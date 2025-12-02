
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

# Bass line (Marcus) - walking line in F, chromatic approach to F#
bass_notes = [
    (45, 1.5), (46, 1.875), (44, 2.25), (47, 2.625),
    (48, 3.0), (49, 3.375), (47, 3.75), (50, 4.125),
    (51, 4.5), (52, 4.875), (50, 5.25), (53, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    (53, 2.0), (57, 2.0), (60, 2.0), (62, 2.0),  # F7
    (59, 3.0), (63, 3.0), (65, 3.0), (67, 3.0),  # Bb7
    (57, 4.0), (60, 4.0), (62, 4.0), (64, 4.0),  # F7
    (60, 5.0), (64, 5.0), (67, 5.0), (69, 5.0)   # C7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start), (38, start + 0.375), (42, start + 0.375),
        (36, start + 0.75), (38, start + 1.125), (42, start + 1.125),
        (36, start + 1.5), (38, start + 1.875), (42, start + 1.875)
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Saxophone (Dante) - one short motif, make it sing
# F - G - Bb - F (F7 arpeggio, but played as a motif)
sax_notes = [
    (60, 1.5), (62, 1.75), (65, 2.0), (60, 2.25),
    (60, 3.0), (62, 3.25), (65, 3.5), (60, 3.75),
    (60, 4.5), (62, 4.75), (65, 5.0), (60, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
