
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.75), (60, 2.0), (61, 2.25),
    (62, 2.5), (63, 2.75), (60, 3.0), (61, 3.25),
    (62, 3.5), (63, 3.75), (60, 4.0), (61, 4.25),
    (62, 4.5), (63, 4.75), (60, 5.0), (61, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    (62, 2.0), (67, 2.0), (70, 2.0), (72, 2.0),
    # Bar 3: Gm7
    (67, 3.0), (72, 3.0), (74, 3.0), (77, 3.0),
    # Bar 4: Cm7
    (60, 4.0), (65, 4.0), (68, 4.0), (70, 4.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: Motif starts on beat 1 of bar 2, ends on beat 3 of bar 4
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, F, Eb, G
sax_notes = [
    (62, 1.5), (65, 1.875), (63, 2.25), (67, 2.625),
    (62, 3.0), (65, 3.375), (63, 3.75), (67, 4.125),
    (62, 4.5), (65, 4.875), (63, 5.25), (67, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
