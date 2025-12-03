
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
    (36, 0.0), (38, 0.375), (42, 0.1875),
    (36, 0.75), (38, 1.125), (42, 0.9375),
    (36, 1.5), (38, 1.875), (42, 1.6875)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass: walking line with chromatic approaches
# D2 (D) -> Eb2 (chromatic) -> G2 (Fifth of Dm) -> G#2 (chromatic)
bass_notes = [
    (38, 1.5, 0.125), (39, 1.625, 0.125), (43, 1.75, 0.125), (44, 1.875, 0.125),
]
for pitch, time, duration in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm9 (D, F, A, C, E)
piano_notes = [
    (50, 1.5, 0.125), (53, 1.5, 0.125), (57, 1.5, 0.125), (60, 1.5, 0.125), (62, 1.5, 0.125)
]
for pitch, time, duration in piano_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging.
# Dm7 motif: D, F, G, Bb (half note, quarter note, eighth note, eighth note)
sax_notes = [
    (62, 1.5, 0.5), (64, 2.0, 0.25), (67, 2.25, 0.125), (65, 2.375, 0.125)
]
for pitch, time, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus on bass: D2 -> C#2 -> F2 -> F#2
bass_notes = [
    (38, 3.0, 0.125), (37, 3.125, 0.125), (43, 3.25, 0.125), (44, 3.375, 0.125)
]
for pitch, time, duration in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)

# Diane on piano: Gm7 (G, Bb, D, F)
piano_notes = [
    (67, 3.0, 0.125), (70, 3.0, 0.125), (62, 3.0, 0.125), (64, 3.0, 0.125)
]
for pitch, time, duration in piano_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# Dante on sax: Repeat the motif with a slight variation, incomplete
sax_notes = [
    (62, 3.0, 0.5), (64, 3.5, 0.25), (67, 3.75, 0.125)
]
for pitch, time, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus on bass: F2 -> E2 -> A2 -> Bb2
bass_notes = [
    (43, 4.5, 0.125), (41, 4.625, 0.125), (48, 4.75, 0.125), (47, 4.875, 0.125)
]
for pitch, time, duration in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)

# Diane on piano: C7 (C, E, G, B)
piano_notes = [
    (60, 4.5, 0.125), (64, 4.5, 0.125), (67, 4.5, 0.125), (71, 4.5, 0.125)
]
for pitch, time, duration in piano_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# Dante on sax: End the motif, leave it open
sax_notes = [
    (62, 4.5, 0.5), (64, 5.0, 0.25), (67, 5.25, 0.125)
]
for pitch, time, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Full drum pattern for bar 4
drum_notes = [
    (36, 4.5, 0.125), (38, 4.875, 0.125), (42, 4.6875, 0.125),
    (36, 5.25, 0.125), (38, 5.625, 0.125), (42, 5.4375, 0.125),
    (36, 5.875, 0.125), (38, 6.0, 0.125), (42, 5.9375, 0.125)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
