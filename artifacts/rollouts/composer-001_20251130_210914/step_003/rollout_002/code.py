
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
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in Fm
bass_notes = [
    (39, 1.5), (40, 1.875), (41, 2.25), (37, 2.625),  # Fm root motion
    (39, 3.0), (40, 3.375), (41, 3.75), (37, 4.125),
    (39, 4.5), (40, 4.875), (41, 5.25), (37, 5.625)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Diane - Comping on 2 and 4 with 7th chords
# Fm7 = F, Ab, C, Eb
# Bbm7 = Bb, Db, F, Ab
# Ebm7 = Eb, Gb, Bb, Db
# Abm7 = Ab, B, Eb, Gb
piano_notes = [
    # Bar 2: Fm7 on beat 2
    (53, 2.0), (51, 2.0), (58, 2.0), (55, 2.0),
    # Bar 3: Bbm7 on beat 2
    (57, 3.0), (50, 3.0), (53, 3.0), (51, 3.0),
    # Bar 4: Ebm7 on beat 2
    (55, 4.0), (53, 4.0), (57, 4.0), (50, 4.0)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(n)

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Dante - Tenor sax: short motif, start it, leave it hanging, finish it
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F -> Gb -> Ab -> F
motif = [
    (53, 1.5), (52, 1.5), (50, 1.5),
    (53, 1.5), (52, 1.5), (50, 1.5),
    (53, 3.0), (52, 3.0), (50, 3.0),
    (53, 4.5), (52, 4.5), (50, 4.5)
]
for note, time in motif:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
