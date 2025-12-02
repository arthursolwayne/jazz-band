
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: C D Eb C (D minor motif)
sax_notes = [
    (60, 1.5), (62, 1.875), (63, 2.25), (60, 2.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: Walking line in D minor
bass_notes = [
    (62, 1.5), (63, 1.875), (60, 2.25), (62, 2.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4 (Dm7, G7)
piano_notes = [
    (62, 1.875), (67, 1.875), (71, 1.875), (74, 1.875),
    (67, 2.625), (72, 2.625), (76, 2.625), (79, 2.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif with a slight variation
sax_notes = [
    (60, 3.0), (62, 3.375), (63, 3.75), (60, 4.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: Walking line in D minor
bass_notes = [
    (62, 3.0), (63, 3.375), (60, 3.75), (62, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4 (Dm7, G7)
piano_notes = [
    (62, 3.375), (67, 3.375), (71, 3.375), (74, 3.375),
    (67, 4.125), (72, 4.125), (76, 4.125), (79, 4.125)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Resolve the motif
sax_notes = [
    (60, 4.5), (62, 4.875), (64, 5.25), (67, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: Walking line in D minor
bass_notes = [
    (62, 4.5), (63, 4.875), (60, 5.25), (62, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4 (Dm7, G7)
piano_notes = [
    (62, 4.875), (67, 4.875), (71, 4.875), (74, 4.875),
    (67, 5.625), (72, 5.625), (76, 5.625), (79, 5.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: Continue the pattern
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
