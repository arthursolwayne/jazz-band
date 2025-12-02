
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
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    (40, 1.5), (41, 1.875), (42, 2.25), (40, 2.625),
    (40, 2.625), (41, 2.875), (42, 3.125), (39, 3.5),
    (40, 3.5), (41, 3.875), (42, 4.25), (40, 4.625),
    (40, 4.625), (41, 4.875), (42, 5.125), (39, 5.5),
    (40, 5.5), (41, 5.875), (42, 6.25), (40, 6.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (43, 2.0), (45, 2.0), (47, 2.0), (48, 2.0),  # Fm7
    # Bar 3
    (43, 3.5), (45, 3.5), (47, 3.5), (48, 3.5),  # Fm7
    # Bar 4
    (43, 5.0), (45, 5.0), (47, 5.0), (48, 5.0)   # Fm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Sax (Dante) - motif in Fm
# Start at 1.5s: F, Ab, Bb, G
# End at 2.625s: F, Bb
# Leave it hanging at 2.625s
sax_notes = [
    (43, 1.5), (41, 1.875), (42, 2.25), (45, 2.625),
    (43, 3.5), (42, 3.875), (45, 4.25),
    (43, 5.25), (42, 5.625), (45, 6.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
