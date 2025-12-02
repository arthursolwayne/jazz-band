
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

# Bass line - walking line with chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.875), (43, 2.25), (44, 2.625),
    (45, 3.0), (46, 3.375), (43, 3.75), (44, 4.125),
    (45, 4.5), (46, 4.875), (43, 5.25), (44, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano - 7th chords on 2 and 4
piano_notes = [
    (57, 2.0), (60, 2.0), (62, 2.0), (64, 2.0),  # C7
    (59, 3.0), (62, 3.0), (64, 3.0), (66, 3.0),  # E7
    (60, 4.0), (64, 4.0), (67, 4.0), (69, 4.0),  # G7
    (62, 5.0), (66, 5.0), (69, 5.0), (71, 5.0)   # B7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax - motif: F, Bb, Eb, D
sax_notes = [
    (84, 1.5), (76, 1.875), (72, 2.25), (71, 2.625),
    (84, 3.5), (76, 3.875), (72, 4.25), (71, 4.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
