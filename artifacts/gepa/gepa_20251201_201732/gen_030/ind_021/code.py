
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
# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.75), (38, 2.0), (41, 2.25),
    (43, 2.5), (41, 2.75), (40, 3.0), (38, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: open voicings, different chord each bar
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (65, 1.5), (68, 1.5), (67, 1.5), (69, 1.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: motif in F, start it and leave it hanging
sax_notes = [
    (66, 1.5), (69, 1.75), (67, 2.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line
bass_notes = [
    (43, 3.0), (41, 3.25), (40, 3.5), (38, 3.75),
    (40, 4.0), (42, 4.25), (40, 4.5), (38, 4.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Bm7 (B, D, F#, A)
piano_notes = [
    (62, 3.0), (64, 3.0), (66, 3.0), (69, 3.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: continue motif
sax_notes = [
    (68, 3.0), (70, 3.25), (68, 3.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line
bass_notes = [
    (38, 4.5), (40, 4.75), (38, 5.0), (41, 5.25),
    (43, 5.5), (41, 5.75), (40, 6.0), (38, 6.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: G7 (G, B, D, F)
piano_notes = [
    (67, 4.5), (69, 4.5), (64, 4.5), (67, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: finish the motif
sax_notes = [
    (67, 4.5), (69, 4.75), (67, 5.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
