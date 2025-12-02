
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
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    (39, 1.5), (40, 1.875), (39, 2.25), (37, 2.625),
    (39, 2.625), (40, 2.875), (39, 3.125), (37, 3.5),
    (39, 3.5), (40, 3.875), (39, 4.25), (37, 4.625),
    (39, 4.625), (40, 4.875), (39, 5.125), (37, 5.5)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comping on Fm7, Bbm7, Ebm7, Abm7
piano_notes = [
    # Bar 2: Fm7 (F, Ab, Bb, Db) on beat 2
    (53, 2.0), (55, 2.0), (57, 2.0), (59, 2.0),
    # Bar 2: Bbm7 (Bb, Db, Eb, F) on beat 4
    (57, 2.5), (59, 2.5), (60, 2.5), (53, 2.5),
    # Bar 3: Ebm7 (Eb, Gb, Ab, Bb) on beat 2
    (60, 3.0), (62, 3.0), (57, 3.0), (55, 3.0),
    # Bar 3: Abm7 (Ab, B, Bb, Db) on beat 4
    (57, 3.5), (59, 3.5), (55, 3.5), (62, 3.5),
    # Bar 4: Fm7 again on beat 2
    (53, 4.0), (55, 4.0), (57, 4.0), (59, 4.0),
    # Bar 4: Bbm7 again on beat 4
    (57, 4.5), (59, 4.5), (60, 4.5), (53, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: short motif, make it sing
# Fm scale: F, Gb, Ab, Bb, B, Db, Eb
# Motif: F (1.5), Ab (1.75), Bb (2.0), F (3.0), Ab (3.25), Bb (3.5), F (4.5), Ab (4.75), Bb (5.0)
sax_notes = [
    (53, 1.5), (57, 1.75), (55, 2.0),
    (53, 3.0), (57, 3.25), (55, 3.5),
    (53, 4.5), (57, 4.75), (55, 5.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("fm_intro.mid")
