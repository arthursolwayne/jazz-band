
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 0.875), (42, 0.75), (42, 0.875), (42, 1.125), (42, 1.25),
    (42, 1.375), (42, 1.5)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line in Dm, chromatic approach on beat 3
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (60, 2.625),  # Dm7
    (62, 3.0), (64, 3.375), (63, 3.75), (60, 4.125)   # Dm7
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4, comp on Dm7
piano_notes = [
    # Bar 2: Dm7 (beat 2)
    (62, 2.0), (67, 2.0), (65, 2.0), (60, 2.0),
    # Bar 2: comp on beat 4
    (62, 2.75), (67, 2.75), (65, 2.75), (60, 2.75),
    # Bar 3: Dm7 (beat 2)
    (62, 3.5), (67, 3.5), (65, 3.5), (60, 3.5),
    # Bar 3: comp on beat 4
    (62, 4.25), (67, 4.25), (65, 4.25), (60, 4.25)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax: Motif: D - F - G - Eb (Dm), then leave it hanging
sax_notes = [
    (62, 1.5), (64, 1.875), (65, 2.25), (63, 2.625),  # D - F - G - Eb
    (62, 3.0), (64, 3.375), (65, 3.75), (63, 4.125)   # repeat
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: walking line in Dm, chromatic approach on beat 3
bass_notes = [
    (62, 3.0), (64, 3.375), (63, 3.75), (60, 4.125),  # Dm7
    (62, 4.5), (64, 4.875), (63, 5.25), (60, 5.625)   # Dm7
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4, comp on Dm7
piano_notes = [
    # Bar 3: Dm7 (beat 2)
    (62, 3.5), (67, 3.5), (65, 3.5), (60, 3.5),
    # Bar 3: comp on beat 4
    (62, 4.25), (67, 4.25), (65, 4.25), (60, 4.25),
    # Bar 4: Dm7 (beat 2)
    (62, 4.75), (67, 4.75), (65, 4.75), (60, 4.75),
    # Bar 4: comp on beat 4
    (62, 5.5), (67, 5.5), (65, 5.5), (60, 5.5)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax: Motif: D - F - G - Eb (Dm), then finish it
sax_notes = [
    (62, 3.0), (64, 3.375), (65, 3.75), (63, 4.125),  # D - F - G - Eb
    (62, 4.5), (64, 4.875), (65, 5.25), (63, 5.625)   # repeat
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875),
    (36, 5.25), (38, 5.375), (42, 5.25), (42, 5.375), (42, 5.625), (42, 5.75),
    (42, 5.875), (42, 6.0)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bass line: walking line in Dm, chromatic approach on beat 3
bass_notes = [
    (62, 4.5), (64, 4.875), (63, 5.25), (60, 5.625),  # Dm7
    (62, 6.0), (64, 6.375), (63, 6.75), (60, 7.125)   # Dm7
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4, comp on Dm7
piano_notes = [
    # Bar 4: Dm7 (beat 2)
    (62, 5.0), (67, 5.0), (65, 5.0), (60, 5.0),
    # Bar 4: comp on beat 4
    (62, 5.75), (67, 5.75), (65, 5.75), (60, 5.75)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax: Motif: D - F - G - Eb (Dm), then finish it
sax_notes = [
    (62, 4.5), (64, 4.875), (65, 5.25), (63, 5.625),  # D - F - G - Eb
    (62, 6.0), (64, 6.375), (65, 6.75), (63, 7.125)   # repeat
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
