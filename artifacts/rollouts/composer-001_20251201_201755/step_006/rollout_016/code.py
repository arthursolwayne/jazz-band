
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Fm (D2-G2, MIDI 38-43)
bass_notes = [
    (38, 1.5, 0.375),   # D2 on 1
    (41, 1.875, 0.375), # F2 on 2
    (43, 2.25, 0.375),  # G2 on 3
    (38, 2.625, 0.375), # D2 on 4
    (40, 3.0, 0.375),   # E2 on 1
    (43, 3.375, 0.375), # G2 on 2
    (38, 3.75, 0.375),  # D2 on 3
    (41, 4.125, 0.375), # F2 on 4
    (43, 4.5, 0.375),   # G2 on 1
    (40, 4.875, 0.375), # E2 on 2
    (38, 5.25, 0.375),  # D2 on 3
    (41, 5.625, 0.375)  # F2 on 4
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (53, 1.5, 0.375), # F
    (60, 1.5, 0.375), # C
    (64, 1.5, 0.375), # D
    (62, 1.5, 0.375), # Ab
    (60, 1.875, 0.375), # C
    (56, 1.875, 0.375), # Bb (chromatic approach)
    (53, 1.875, 0.375), # F
    (64, 1.875, 0.375), # D
    (64, 2.25, 0.375), # D
    (60, 2.25, 0.375), # C
    (56, 2.25, 0.375), # Bb
    (53, 2.25, 0.375), # F
    (62, 2.625, 0.375), # Ab
    (60, 2.625, 0.375), # C
    (53, 2.625, 0.375), # F
    (64, 2.625, 0.375), # D
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums (bars 2-4)
drum_notes = [
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.5, 0.375),   # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.375), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.375), # Hihat on 4
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.375),   # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.375), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.375), # Hihat on 4
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.375),   # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.375), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.375)  # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F (Fm7 intervallic movement)
sax_notes = [
    (53, 1.5, 0.375), # F
    (62, 1.875, 0.375), # Ab
    (60, 2.25, 0.375), # Bb
    (53, 2.625, 0.375), # F
    (53, 3.0, 0.375), # F (return)
    (62, 3.375, 0.375), # Ab
    (60, 3.75, 0.375), # Bb
    (53, 4.125, 0.375), # F
    (53, 4.5, 0.375), # F
    (62, 4.875, 0.375), # Ab
    (60, 5.25, 0.375), # Bb
    (53, 5.625, 0.375)  # F
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
