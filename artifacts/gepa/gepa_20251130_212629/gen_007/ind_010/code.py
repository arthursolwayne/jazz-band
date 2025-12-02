
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

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    (57, 1.5), (59, 1.875), (58, 2.25), (56, 2.625),
    (57, 3.0), (59, 3.375), (58, 3.75), (56, 4.125),
    (57, 4.5), (59, 4.875), (58, 5.25), (56, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano (Diane) - 7th chords on 2 and 4
# Fm7 on beat 2 (bar 2), Cm7 on beat 2 (bar 3), Gm7 on beat 2 (bar 4)
piano_notes = [
    # Bar 2
    (57, 2.0), (60, 2.0), (62, 2.0), (64, 2.0),  # Fm7
    # Bar 3
    (58, 3.375), (60, 3.375), (62, 3.375), (65, 3.375),  # Cm7
    # Bar 4
    (59, 4.875), (60, 4.875), (62, 4.875), (67, 4.875),  # Gm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    # Bar 3
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    # Bar 4
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax (Dante) - motif in Fm
# Fm (F, Ab, Bb, D) - short motif
# Start with F, then Bb, then a chromatic line up to D
# Then leave it hanging
sax_notes = [
    (57, 1.5), (62, 1.875), (60, 2.25), (61, 2.625),
    (62, 3.0), (63, 3.375), (64, 3.75), (65, 4.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
