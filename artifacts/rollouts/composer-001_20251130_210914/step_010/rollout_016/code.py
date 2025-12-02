
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
    (36, 1.125), (38, 1.5), (42, 1.5),
    (36, 2.0), (38, 2.375), (42, 2.375),
    (36, 3.125), (38, 3.5), (42, 3.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D D# F A (D minor pentatonic with a raised 4th)
sax_notes = [
    (62, 1.5, 0.5), (63, 2.0, 0.5), (65, 2.5, 0.5), (69, 3.0, 0.5),
    (62, 3.5, 0.5), (63, 4.0, 0.5), (65, 4.5, 0.5), (69, 5.0, 0.5)
]
for pitch, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration))

# Bass: Walking line, chromatic approaches, never the same note twice (D D# C# D F)
bass_notes = [
    (62, 1.5, 0.25), (63, 1.75, 0.25), (61, 2.0, 0.25), (62, 2.25, 0.25),
    (65, 2.5, 0.25), (66, 2.75, 0.25), (64, 3.0, 0.25), (65, 3.25, 0.25),
    (62, 3.5, 0.25), (63, 3.75, 0.25), (61, 4.0, 0.25), (62, 4.25, 0.25),
    (65, 4.5, 0.25), (66, 4.75, 0.25), (64, 5.0, 0.25), (65, 5.25, 0.25)
]
for pitch, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
# D7 (D F# A C) on beat 2 and 4
piano_notes = [
    (62, 2.0, 0.25), (67, 2.0, 0.25), (69, 2.0, 0.25), (64, 2.0, 0.25),
    (62, 4.0, 0.25), (67, 4.0, 0.25), (69, 4.0, 0.25), (64, 4.0, 0.25)
]
for pitch, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    (36, 1.5, 0.125), (38, 1.875, 0.125), (42, 1.875, 0.125),
    (36, 2.625, 0.125), (38, 3.0, 0.125), (42, 3.0, 0.125),
    (36, 3.75, 0.125), (38, 4.125, 0.125), (42, 4.125, 0.125),
    (36, 4.875, 0.125), (38, 5.25, 0.125), (42, 5.25, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
