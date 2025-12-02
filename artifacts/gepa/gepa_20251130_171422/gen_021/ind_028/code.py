
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
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches
bass_notes = [
    (39, 1.5), (40, 1.875), (38, 2.25), (36, 2.625),
    (37, 3.0), (39, 3.375), (40, 3.75), (38, 4.125),
    (36, 4.5), (37, 4.875), (40, 5.25), (38, 5.625)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano chords: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    (53, 2.0), (50, 2.0), (48, 2.0), (46, 2.0),
    # Bar 3: Bb7 on beat 2
    (57, 3.5), (54, 3.5), (52, 3.5), (50, 3.5),
    # Bar 4: Eb7 on beat 2
    (60, 5.0), (57, 5.0), (55, 5.0), (53, 5.0)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax solo: One short motif, start it, leave it hanging, come back and finish it
# Fm scale: F, Gb, Ab, Bb, B, C, Db
# Motif: F - Bb - Ab - Gb
sax_notes = [
    (53, 1.5), (50, 1.5), (48, 1.5), (47, 1.5),
    (53, 2.25), (50, 2.25), (48, 2.25), (47, 2.25),
    (53, 3.0), (50, 3.0), (48, 3.0), (47, 3.0),
    (53, 3.75), (50, 3.75), (48, 3.75), (47, 3.75)
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
