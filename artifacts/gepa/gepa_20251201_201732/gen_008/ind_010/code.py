
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.375, 0.125), # Hihat on &1
    (38, 0.75, 0.375),  # Snare on 2
    (42, 0.875, 0.125), # Hihat on &2
    (36, 1.125, 0.375), # Kick on 3
    (42, 1.5, 0.125)    # Hihat on &3
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # D2 on 1
    (41, 1.875, 0.375), # F#2 on 2 (chromatic approach)
    (43, 2.25, 0.375),  # A2 on 3
    (40, 2.625, 0.375), # G2 on 4
    (38, 3.0, 0.375),   # D2 on 1
    (41, 3.375, 0.375), # F#2 on 2
    (43, 3.75, 0.375),  # A2 on 3
    (40, 4.125, 0.375), # G2 on 4
    (38, 4.5, 0.375),   # D2 on 1
    (41, 4.875, 0.375), # F#2 on 2
    (43, 5.25, 0.375),  # A2 on 3
    (40, 5.625, 0.375)  # G2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (D, F#, A, C#)
    (62, 1.5, 0.375),  # D4
    (67, 1.5, 0.375),  # F#4
    (71, 1.5, 0.375),  # A4
    (64, 1.5, 0.375),  # C#4
    # Bar 3: Gm7 (G, Bb, D, F)
    (67, 2.25, 0.375), # G4
    (71, 2.25, 0.375), # Bb4
    (74, 2.25, 0.375), # D5
    (69, 2.25, 0.375), # F4
    # Bar 4: A7 (A, C#, E, G#)
    (71, 3.0, 0.375),  # A4
    (76, 3.0, 0.375),  # C#5
    (76, 3.0, 0.375),  # E5 (duplicated for emphasis)
    (74, 3.0, 0.375),  # G#4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.5, 0.125),   # Hihat on 1
    (42, 1.625, 0.125), # Hihat on &1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.125), # Hihat on 2
    (42, 1.975, 0.125), # Hihat on &2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.125),  # Hihat on 3
    (42, 2.375, 0.125), # Hihat on &3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.125), # Hihat on 4
    (42, 2.75, 0.125),  # Hihat on &4
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.125),   # Hihat on 1
    (42, 3.125, 0.125), # Hihat on &1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.125), # Hihat on 2
    (42, 3.475, 0.125), # Hihat on &2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.125),  # Hihat on 3
    (42, 3.875, 0.125), # Hihat on &3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.125), # Hihat on 4
    (42, 4.25, 0.125),  # Hihat on &4
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.125),   # Hihat on 1
    (42, 4.625, 0.125), # Hihat on &1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.125), # Hihat on 2
    (42, 4.975, 0.125), # Hihat on &2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.125),  # Hihat on 3
    (42, 5.375, 0.125), # Hihat on &3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.125), # Hihat on 4
    (42, 5.75, 0.125)   # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (72, 1.5, 0.5),      # D5
    (76, 2.0, 0.25),     # F#5
    (72, 2.25, 0.25),    # D5
    (76, 2.5, 0.25),     # F#5
    (72, 2.75, 0.25),    # D5
    (76, 3.0, 0.25),     # F#5
    (72, 3.25, 0.25),    # D5
    (76, 3.5, 0.25),     # F#5
    (72, 3.75, 0.25),    # D5
    (76, 4.0, 0.25),     # F#5
    (72, 4.25, 0.25),    # D5
    (76, 4.5, 0.25),     # F#5
    (72, 4.75, 0.25),    # D5
    (76, 5.0, 0.25),     # F#5
    (72, 5.25, 0.25),    # D5
    (76, 5.5, 0.25)      # F#5
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
