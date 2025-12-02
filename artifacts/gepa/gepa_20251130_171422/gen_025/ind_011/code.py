
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
    (36, 1.0, 1.0),  # Kick on 1
    (42, 1.0, 0.5),  # Hihat on 1
    (42, 1.25, 0.5), # Hihat on 2
    (36, 1.5, 1.0),  # Kick on 3
    (42, 1.5, 0.5),  # Hihat on 3
    (42, 1.75, 0.5), # Hihat on 4
]
for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approach
bass_notes = [
    (34, 1.5, 0.375), # F
    (35, 1.875, 0.375), # Gb
    (36, 2.25, 0.375), # G
    (37, 2.625, 0.375), # Ab
]
for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (60, 1.875, 0.375), # C (F7)
    (62, 1.875, 0.375), # D
    (64, 1.875, 0.375), # E
    (67, 1.875, 0.375), # G
    (60, 2.625, 0.375), # C (F7)
    (62, 2.625, 0.375), # D
    (64, 2.625, 0.375), # E
    (67, 2.625, 0.375), # G
]
for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Sax: Motif - sparse, expressive
sax_notes = [
    (60, 1.5, 0.75), # C (F7)
    (62, 2.25, 0.75), # D (F7)
    (64, 3.0, 0.75), # E (F7)
    (66, 3.75, 0.75), # G (F7)
]
for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approach
bass_notes = [
    (38, 3.0, 0.375), # Bb
    (39, 3.375, 0.375), # B
    (40, 3.75, 0.375), # C
    (41, 4.125, 0.375), # C#
]
for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (60, 3.375, 0.375), # C (F7)
    (62, 3.375, 0.375), # D
    (64, 3.375, 0.375), # E
    (67, 3.375, 0.375), # G
    (60, 4.125, 0.375), # C (F7)
    (62, 4.125, 0.375), # D
    (64, 4.125, 0.375), # E
    (67, 4.125, 0.375), # G
]
for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Sax: Continue motif with variation
sax_notes = [
    (64, 3.0, 0.75), # E (F7)
    (66, 3.75, 0.75), # G (F7)
    (67, 4.5, 0.75), # G (F7)
    (66, 5.25, 0.75), # G (F7)
]
for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 1.0),  # Kick on 1
    (42, 3.0, 0.5),  # Hihat on 1
    (42, 3.25, 0.5), # Hihat on 2
    (38, 3.5, 1.0),  # Snare on 2
    (42, 3.5, 0.5),  # Hihat on 3
    (42, 3.75, 0.5), # Hihat on 4
    (36, 4.0, 1.0),  # Kick on 3
    (42, 4.0, 0.5),  # Hihat on 4
    (42, 4.25, 0.5), # Hihat on 4
    (38, 4.5, 1.0),  # Snare on 4
]
for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approach
bass_notes = [
    (43, 4.5, 0.375), # Db
    (44, 4.875, 0.375), # D
    (45, 5.25, 0.375), # Eb
    (47, 5.625, 0.375), # F
]
for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (60, 4.875, 0.375), # C (F7)
    (62, 4.875, 0.375), # D
    (64, 4.875, 0.375), # E
    (67, 4.875, 0.375), # G
    (60, 5.625, 0.375), # C (F7)
    (62, 5.625, 0.375), # D
    (64, 5.625, 0.375), # E
    (67, 5.625, 0.375), # G
]
for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Sax: Motif variation with space and dynamic shift
sax_notes = [
    (67, 4.5, 0.75), # G (F7)
    (66, 5.25, 0.75), # G (F7)
    (64, 6.0, 0.75), # E (F7)
]
for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 1.0),  # Kick on 1
    (42, 4.5, 0.5),  # Hihat on 1
    (42, 4.75, 0.5), # Hihat on 2
    (38, 5.0, 1.0),  # Snare on 2
    (42, 5.0, 0.5),  # Hihat on 3
    (42, 5.25, 0.5), # Hihat on 4
    (36, 5.5, 1.0),  # Kick on 3
    (42, 5.5, 0.5),  # Hihat on 4
    (42, 5.75, 0.5), # Hihat on 4
    (38, 6.0, 1.0),  # Snare on 4
]
for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
