
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

# Bass line: walking line in Dm (D2-G2), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.875), (39, 2.25), (42, 2.625),
    (43, 3.0), (41, 3.375), (40, 3.75), (38, 4.125),
    (38, 4.5), (40, 4.875), (39, 5.25), (42, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, F)
piano_notes = [
    (62, 1.5), (65, 1.5), (67, 1.5), (69, 1.5),  # Dm7
    (62, 2.0), (65, 2.0), (67, 2.0), (69, 2.0),  # Dm7
    (62, 2.5), (65, 2.5), (67, 2.5), (69, 2.5),  # Dm7
    (62, 3.0), (65, 3.0), (67, 3.0), (69, 3.0)   # Dm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Bar 3: G7 (B, D, G, B)
piano_notes = [
    (67, 3.5), (69, 3.5), (71, 3.5), (73, 3.5),  # G7
    (67, 4.0), (69, 4.0), (71, 4.0), (73, 4.0),  # G7
    (67, 4.5), (69, 4.5), (71, 4.5), (73, 4.5),  # G7
    (67, 5.0), (69, 5.0), (71, 5.0), (73, 5.0)   # G7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Bar 4: Cm7 (E, G, C, E)
piano_notes = [
    (64, 5.5), (67, 5.5), (69, 5.5), (72, 5.5),  # Cm7
    (64, 6.0), (67, 6.0), (69, 6.0), (72, 6.0),  # Cm7
    (64, 6.5), (67, 6.5), (69, 6.5), (72, 6.5),  # Cm7
    (64, 7.0), (67, 7.0), (69, 7.0), (72, 7.0)   # Cm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, E, F, G, A, B, C, D
# Motif: D, E, F, D (half note, quarter note, eighth note, eighth note)
sax_notes = [
    (62, 1.5, 1.0),  # D (half note)
    (64, 2.0, 0.5),  # E (quarter note)
    (65, 2.5, 0.25), # F (eighth note)
    (62, 2.75, 0.25) # D (eighth note)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
