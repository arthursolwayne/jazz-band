
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on 2
    (42, 0.375, 0.1875), # Hihat on 3
    (42, 0.5625, 0.1875), # Hihat on 4
    (36, 1.125, 0.375), # Kick on 3
    (38, 1.5, 0.375), # Snare on 4
    (42, 1.125, 0.1875), # Hihat on 3
    (42, 1.3125, 0.1875), # Hihat on 4
    (42, 1.5, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375), # D2
    (40, 1.875, 0.375), # F2 (chromatic approach)
    (43, 2.25, 0.375), # A2 (fifth of Dm)
    (41, 2.625, 0.375), # G2 (chromatic approach)
    (38, 3.0, 0.375), # D2
    (40, 3.375, 0.375), # F2
    (43, 3.75, 0.375), # A2
    (41, 4.125, 0.375), # G2
    (38, 4.5, 0.375), # D2
    (40, 4.875, 0.375), # F2
    (43, 5.25, 0.375), # A2
    (41, 5.625, 0.375) # G2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F#-D-Bb-F)
piano_notes = [
    (57, 1.5, 0.375), # F#
    (50, 1.5, 0.375), # D
    (62, 1.5, 0.375), # Bb
    (55, 1.5, 0.375), # F
    (57, 1.5, 0.375), # F#
    (62, 1.5, 0.375), # Bb
    (55, 1.5, 0.375), # F
]
# Bar 3: Gm7 (Bb-G-D-F)
piano_notes.extend([
    (53, 2.25, 0.375), # Bb
    (50, 2.25, 0.375), # G
    (55, 2.25, 0.375), # D
    (55, 2.25, 0.375), # F
    (53, 2.25, 0.375), # Bb
    (55, 2.25, 0.375), # F
    (50, 2.25, 0.375), # G
])
# Bar 4: Cm7 (Eb-C-G-Bb)
piano_notes.extend([
    (53, 3.0, 0.375), # Eb
    (52, 3.0, 0.375), # C
    (55, 3.0, 0.375), # G
    (57, 3.0, 0.375), # Bb
    (53, 3.0, 0.375), # Eb
    (55, 3.0, 0.375), # G
    (52, 3.0, 0.375), # C
])
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (E3), Bb (D4), F (E4), D (D4), leave it hanging on F (F4) then return to D (E3)
sax_notes = [
    (62, 1.5, 0.375), # D (E3)
    (64, 1.875, 0.375), # Bb (D4)
    (65, 2.25, 0.375), # F (E4)
    (64, 2.625, 0.375), # D (D4)
    (65, 3.0, 0.375), # F (F4)
    (65, 3.375, 0.375), # F (F4)
    (65, 3.75, 0.375), # F (F4)
    (65, 4.125, 0.375), # F (F4)
    (65, 4.5, 0.375), # F (F4)
    (62, 4.875, 0.375), # D (E3)
    (64, 5.25, 0.375), # Bb (D4)
    (65, 5.625, 0.375) # F (E4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
