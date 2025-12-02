
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
# Bass line - Marcus: walking line, chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.875), (44, 2.25), (43, 2.625),
    (45, 3.0), (46, 3.375), (44, 3.75), (43, 4.125),
    (45, 4.5), (46, 4.875), (44, 5.25), (43, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 3.0), (67, 3.0), (60, 3.0), (64, 3.0),  # F7 on beat 2
    (62, 4.5), (67, 4.5), (60, 4.5), (64, 4.5),  # F7 on beat 4
    (62, 4.0), (67, 4.0), (60, 4.0), (64, 4.0)   # F7 on beat 3, just before end
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Sax - Dante: short motif, make it sing
# F - A - Bb - F (melody)
sax_notes = [
    (87, 1.5), (92, 1.875), (90, 2.25), (87, 2.625),  # First pass
    (87, 3.0), (92, 3.375), (90, 3.75), (87, 4.125),  # Second pass
    (87, 4.5), (92, 4.875), (90, 5.25), (87, 5.625)   # Third pass
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_piece.mid")
