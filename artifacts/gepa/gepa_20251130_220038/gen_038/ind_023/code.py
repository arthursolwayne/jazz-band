
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.875), (44, 2.25), (43, 2.625),
    (45, 3.0), (47, 3.375), (46, 3.75), (44, 4.125),
    (45, 4.5), (46, 4.875), (43, 5.25), (42, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 2.0), (67, 2.0), (64, 2.0), (69, 2.0),  # D7
    (62, 3.0), (67, 3.0), (64, 3.0), (69, 3.0),  # D7
    (62, 4.0), (67, 4.0), (64, 4.0), (69, 4.0),  # D7
    (62, 5.0), (67, 5.0), (64, 5.0), (69, 5.0)   # D7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375))

# Sax: Whisper to cry, one short motif
# F - G# - Bb - F (F7sus4)
sax_notes = [
    (84, 1.5), (86, 1.875), (82, 2.25), (84, 2.625),  # First phrase
    (84, 3.0), (87, 3.375), (82, 3.75), (84, 4.125),  # Second phrase
    (84, 4.5), (86, 4.875), (82, 5.25), (84, 5.625)   # Third phrase
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
