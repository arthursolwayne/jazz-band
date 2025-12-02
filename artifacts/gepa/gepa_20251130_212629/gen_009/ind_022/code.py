
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

# Bars 2-4 (1.5 - 6.0s)
# Bass line: walking line with chromatic approaches
bass_notes = [
    (45, 1.5), (47, 1.875), (46, 2.25), (44, 2.625),
    (45, 2.625), (47, 2.875), (46, 3.25), (44, 3.625),
    (45, 3.625), (47, 3.875), (46, 4.25), (44, 4.625),
    (45, 4.625), (47, 4.875), (46, 5.25), (44, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
# F7, Bb7, F7, Bb7
chords = [
    (58, 1.875), (60, 1.875), (62, 1.875), (64, 1.875),  # F7
    (55, 2.625), (57, 2.625), (59, 2.625), (61, 2.625),  # Bb7
    (58, 3.875), (60, 3.875), (62, 3.875), (64, 3.875),  # F7
    (55, 4.625), (57, 4.625), (59, 4.625), (61, 4.625)   # Bb7
]
for note, time in chords:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Motif in F (F, G#, Bb, F)
sax_notes = [
    (58, 1.5), (61, 1.875), (62, 2.25), (58, 2.625),
    (58, 3.0), (61, 3.375), (62, 3.75), (58, 4.125),
    (58, 4.5), (61, 4.875), (62, 5.25), (58, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
