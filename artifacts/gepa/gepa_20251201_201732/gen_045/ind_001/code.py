
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# ---------------------
# Bar 1: Little Ray alone (0.0 - 1.5s)
# ---------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0),   # Kick on 1
    (38, 0.5),   # Snare on 2
    (36, 1.0),   # Kick on 3
    (38, 1.5),   # Snare on 4
    (42, 0.0),   # Hihat on 1
    (42, 0.375), # Hihat on &
    (42, 0.75),  # Hihat on 2
    (42, 1.125), # Hihat on 2&
    (42, 1.5),   # Hihat on 3
    (42, 1.875), # Hihat on 3&
    (42, 2.25),  # Hihat on 4
    (42, 2.625), # Hihat on 4&
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# ---------------------
# Bars 2-4: Full quartet (1.5 - 6.0s)
# ---------------------
# Bass line: walking in Fm (F, Ab, G, E, D, C, Bb, A)
bass_notes = [
    (53, 1.5),   # F2
    (50, 1.875), # Ab2
    (52, 2.25),  # G2
    (50, 2.625), # E2
    (49, 3.0),   # D2
    (48, 3.375), # C2
    (47, 3.75),  # Bb2
    (46, 4.125), # A2
    (53, 4.5),   # F2
    (50, 4.875), # Ab2
    (52, 5.25),  # G2
    (50, 5.625), # E2
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano chords: open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (53, 1.5),   # F
    (50, 1.5),   # Ab
    (52, 1.5),   # C
    (57, 1.5),   # D
    (58, 1.5),   # F
    (51, 1.5),   # Bb
    (53, 1.5),   # F
    (50, 1.5),   # Ab
    (52, 1.5),   # C
    (57, 1.5),   # D
    (58, 1.5),   # F
    (51, 1.5),   # Bb
]
# Bar 3: Bbm7 (Bb, Db, F, G)
piano_notes.extend([
    (58, 3.0),   # Bb
    (55, 3.0),   # Db
    (53, 3.0),   # F
    (57, 3.0),   # G
    (59, 3.0),   # Bb
    (56, 3.0),   # Eb
    (58, 3.0),   # Bb
    (55, 3.0),   # Db
    (53, 3.0),   # F
    (57, 3.0),   # G
    (59, 3.0),   # Bb
    (56, 3.0),   # Eb
])
# Bar 4: Abmaj7 (Ab, C, Eb, G)
piano_notes.extend([
    (50, 4.5),   # Ab
    (52, 4.5),   # C
    (55, 4.5),   # Eb
    (57, 4.5),   # G
    (51, 4.5),   # Ab
    (53, 4.5),   # C
    (56, 4.5),   # Eb
    (57, 4.5),   # G
    (50, 4.5),   # Ab
    (52, 4.5),   # C
    (55, 4.5),   # Eb
    (57, 4.5),   # G
])
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax melody: one short motif, start on F, leave it hanging
sax_notes = [
    (53, 1.5),   # F
    (57, 1.875), # D
    (52, 2.25),  # G
    (50, 2.625), # Ab
    (53, 3.0),   # F
    (57, 3.375), # D
    (52, 3.75),  # G
    (50, 4.125), # Ab
    (53, 4.5),   # F
    (57, 4.875), # D
    (52, 5.25),  # G
    (50, 5.625), # Ab
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

# Drums continue with the same pattern for bars 2-4
bar2_drum_notes = [
    (36, 1.5),   # Kick on 1
    (38, 2.0),   # Snare on 2
    (36, 2.5),   # Kick on 3
    (38, 3.0),   # Snare on 4
    (36, 3.5),   # Kick on 1
    (38, 4.0),   # Snare on 2
    (36, 4.5),   # Kick on 3
    (38, 5.0),   # Snare on 4
    (42, 1.5),   # Hihat on 1
    (42, 1.875), # Hihat on &
    (42, 2.25),  # Hihat on 2
    (42, 2.625), # Hihat on 2&
    (42, 3.0),   # Hihat on 3
    (42, 3.375), # Hihat on 3&
    (42, 3.75),  # Hihat on 4
    (42, 4.125), # Hihat on 4&
    (42, 4.5),   # Hihat on 1
    (42, 4.875), # Hihat on &
    (42, 5.25),  # Hihat on 2
    (42, 5.625), # Hihat on 2&
]
for note, time in bar2_drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
