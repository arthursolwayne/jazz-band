
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

# Marcus: Walking bass line in Fm (F, Gb, Ab, Bb, Bb, C, Db, Eb, etc.)
bass_notes = [
    (71, 1.5), (69, 1.875), (67, 2.25), (65, 2.625),
    (65, 2.875), (67, 3.25), (69, 3.625), (71, 4.0),
    (71, 4.375), (69, 4.75), (67, 5.125), (65, 5.5)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, Bb, Db)
    (53, 1.875), (50, 1.875), (48, 1.875), (45, 1.875),
    # Bar 3: Bb7 (Bb, Db, Eb, F)
    (48, 3.125), (45, 3.125), (43, 3.125), (53, 3.125),
    # Bar 4: Eb7 (Eb, Gb, Ab, Bb)
    (43, 4.375), (40, 4.375), (48, 4.375), (45, 4.375)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Dante: One short motif, make it sing (F, Ab, Bb, F)
sax_notes = [
    (53, 1.5), (50, 1.875), (48, 2.25), (53, 2.625),
    (50, 3.0), (48, 3.375), (53, 3.75), (50, 4.125),
    (48, 4.5), (53, 4.875)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
