
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375),  # Hihat on 4
    (42, 1.5, 0.375),    # Hihat on 4 end
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),    # F2 (root)
    (40, 1.875, 0.375),  # Ab (chromatic approach)
    (43, 2.25, 0.375),   # C (fifth)
    (38, 2.625, 0.375),  # F2 (root)
    (40, 2.875, 0.375),  # Ab (chromatic approach)
    (43, 3.25, 0.375),   # C (fifth)
    (38, 3.625, 0.375),  # F2 (root)
    (40, 4.0, 0.375),    # Ab (chromatic approach)
    (43, 4.375, 0.375),  # C (fifth)
    (38, 4.75, 0.375),   # F2 (root)
    (40, 5.125, 0.375),  # Ab (chromatic approach)
    (43, 5.5, 0.375),    # C (fifth)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    (53, 1.5, 0.375),  # F (MIDI 53)
    (58, 1.5, 0.375),  # A
    (60, 1.5, 0.375),  # C
    (64, 1.5, 0.375),  # E
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    (57, 2.25, 0.375),  # Bb
    (62, 2.25, 0.375),  # D
    (60, 2.25, 0.375),  # F
    (65, 2.25, 0.375),  # Ab
    # Bar 4: C7 (C, E, G, Bb)
    (60, 3.0, 0.375),  # C
    (64, 3.0, 0.375),  # E
    (67, 3.0, 0.375),  # G
    (65, 3.0, 0.375),  # Bb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.375 + 0.375))
    # Hihat on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.375 + 0.375))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.75 + 0.375))
    # Hihat on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.75 + 0.375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.125 + 0.375))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.125 + 0.375))
    # Hihat on 4 end
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.5 + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (MIDI 53), G (55), E (64)
# Start on bar 2, play F and G on beat 1 and 2, then leave E hanging at the end of bar 3

# Bar 2: F, G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25))

# Bar 3: No notes (leave the E hanging)
# Bar 4: Finish with E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
