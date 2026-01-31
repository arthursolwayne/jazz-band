
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_1_start = 0.0
bar_1_end = 1.5
drum_notes = [
    (36, bar_1_start + 0.0, 0.375),  # Kick
    (38, bar_1_start + 0.375, 0.375),  # Snare
    (42, bar_1_start + 0.0, 0.1875),
    (42, bar_1_start + 0.1875, 0.1875),
    (42, bar_1_start + 0.375, 0.1875),
    (42, bar_1_start + 0.5625, 0.1875),
    (36, bar_1_start + 0.75, 0.375),  # Kick
    (38, bar_1_start + 1.125, 0.375),  # Snare
    (42, bar_1_start + 1.5, 0.1875),
    (42, bar_1_start + 1.6875, 0.1875),
    (42, bar_1_start + 1.875, 0.1875),
    (42, bar_1_start + 2.0625, 0.1875),
]
for note, start, duration in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(note_obj)

# Bar 2: Full quartet starts (1.5 - 3.0s)
# Bass: D2 (MIDI 38) with walking line and chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # D2
    (39, 1.875, 0.375),  # Eb2 (chromatic)
    (40, 2.25, 0.375),  # E2
    (38, 2.625, 0.375),  # D2
]
for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Piano: Open voicings, different chord each bar
# Bar 2: Dm7 (D-F-A-C) in open voicing
piano_notes = [
    (62, 1.5, 0.375),  # D4
    (64, 1.5, 0.375),  # F4
    (67, 1.5, 0.375),  # A4
    (69, 1.5, 0.375),  # C5
]
for note, start, duration in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Sax: Motif starts here, short and singing
sax_notes = [
    (62, 1.5, 0.375),  # D4
    (64, 1.875, 0.375),  # F4
    (62, 2.25, 0.375),  # D4
]
for note, start, duration in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G2 (MIDI 43) with walking line
bass_notes = [
    (43, 3.0, 0.375),  # G2
    (42, 3.375, 0.375),  # F2 (chromatic)
    (43, 3.75, 0.375),  # G2
    (45, 4.125, 0.375),  # Bb2
]
for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Piano: Bm7 (B-D-F#-A) open voicing
piano_notes = [
    (67, 3.0, 0.375),  # B4
    (69, 3.0, 0.375),  # D5
    (71, 3.0, 0.375),  # F#5
    (74, 3.0, 0.375),  # A5
]
for note, start, duration in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Sax: Continue motif
sax_notes = [
    (67, 3.0, 0.375),  # B4
    (69, 3.375, 0.375),  # D5
    (67, 3.75, 0.375),  # B4
]
for note, start, duration in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Drums: Same pattern, kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_3_start = 3.0
bar_3_end = 4.5
for i, note, start, duration in enumerate(drum_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar_3_start + start, end=bar_3_start + start + duration)
    drums.notes.append(note_obj)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: C2 (MIDI 40) with walking line
bass_notes = [
    (40, 4.5, 0.375),  # C2
    (41, 4.875, 0.375),  # Db2 (chromatic)
    (40, 5.25, 0.375),  # C2
    (38, 5.625, 0.375),  # D2
]
for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Piano: Cm7 (C-Eb-G-Bb) open voicing
piano_notes = [
    (60, 4.5, 0.375),  # C4
    (62, 4.5, 0.375),  # Eb4
    (65, 4.5, 0.375),  # G4
    (67, 4.5, 0.375),  # Bb4
]
for note, start, duration in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Sax: Finish motif
sax_notes = [
    (60, 4.5, 0.375),  # C4
    (62, 4.875, 0.375),  # Eb4
    (60, 5.25, 0.375),  # C4
]
for note, start, duration in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Drums: Same pattern
bar_4_start = 4.5
for i, note, start, duration in enumerate(drum_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar_4_start + start, end=bar_4_start + start + duration)
    drums.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
