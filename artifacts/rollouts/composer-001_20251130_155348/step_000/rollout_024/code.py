
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
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif - F (C4), Bb (Bb4), C (C5), Eb (Eb4)
sax_notes = [
    (60, 1.5), (62, 1.875), (64, 2.25), (65, 2.625)
]
for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.875), (64, 2.25), (65, 2.625)
]
for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (64, 1.875), (67, 1.875), (71, 1.875), (72, 1.875),
    (64, 2.625), (67, 2.625), (71, 2.625), (72, 2.625)
]
for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(piano_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif, but with a slight variation
sax_notes = [
    (60, 3.0), (62, 3.375), (64, 3.75), (65, 4.125)
]
for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    (62, 3.0), (63, 3.375), (64, 3.75), (65, 4.125)
]
for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (64, 3.375), (67, 3.375), (71, 3.375), (72, 3.375),
    (64, 4.125), (67, 4.125), (71, 4.125), (72, 4.125)
]
for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(piano_note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif, but resolve to F (C4)
sax_notes = [
    (60, 4.5), (62, 4.875), (64, 5.25), (60, 5.625)
]
for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    (62, 4.5), (63, 4.875), (64, 5.25), (65, 5.625)
]
for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (64, 4.875), (67, 4.875), (71, 4.875), (72, 4.875),
    (64, 5.625), (67, 5.625), (71, 5.625), (72, 5.625)
]
for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(piano_note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('jazz_intro.mid')
