
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
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 0.875), (42, 0.75), (42, 0.875),
    (36, 1.125), (38, 1.25), (42, 1.125), (42, 1.25), (42, 1.375), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Dm7 walking line
bass_notes = [
    (62, 1.5), (60, 1.75), (58, 2.0), (57, 2.25),
    (62, 2.5), (60, 2.75), (58, 3.0), (57, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Dm7 comp on 2 and 4
piano_notes = [
    # Bar 2: 2 and 4
    (67, 1.75), (62, 1.75), (60, 1.75), (64, 1.75),  # Dm7
    (67, 2.5), (62, 2.5), (60, 2.5), (64, 2.5)       # Dm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Dm7 motif
sax_notes = [
    (62, 1.5), (65, 1.625), (62, 1.75), (60, 2.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Dm7 walking line
bass_notes = [
    (62, 3.0), (60, 3.25), (58, 3.5), (57, 3.75),
    (62, 4.0), (60, 4.25), (58, 4.5), (57, 4.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Dm7 comp on 2 and 4
piano_notes = [
    # Bar 3: 2 and 4
    (67, 3.25), (62, 3.25), (60, 3.25), (64, 3.25),  # Dm7
    (67, 4.0), (62, 4.0), (60, 4.0), (64, 4.0)       # Dm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Dm7 motif (reprise)
sax_notes = [
    (62, 3.0), (65, 3.125), (62, 3.25), (60, 3.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 3
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.125), (42, 3.25), (42, 3.375),
    (36, 3.75), (38, 3.875), (42, 3.75), (42, 3.875),
    (36, 4.125), (38, 4.25), (42, 4.125), (42, 4.25), (42, 4.375), (42, 4.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Dm7 walking line
bass_notes = [
    (62, 4.5), (60, 4.75), (58, 5.0), (57, 5.25),
    (62, 5.5), (60, 5.75), (58, 6.0), (57, 6.25)  # Truncate at 6.0
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=min(time + 0.25, 6.0)))

# Piano: Dm7 comp on 2 and 4
piano_notes = [
    # Bar 4: 2 and 4
    (67, 4.75), (62, 4.75), (60, 4.75), (64, 4.75),  # Dm7
    (67, 5.5), (62, 5.5), (60, 5.5), (64, 5.5)       # Dm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Dm7 motif (finish it)
sax_notes = [
    (62, 4.5), (65, 4.625), (62, 4.75), (60, 5.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 4
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875),
    (36, 5.25), (38, 5.375), (42, 5.25), (42, 5.375),
    (36, 5.625), (38, 5.75), (42, 5.625), (42, 5.75), (42, 5.875), (42, 6.0)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
