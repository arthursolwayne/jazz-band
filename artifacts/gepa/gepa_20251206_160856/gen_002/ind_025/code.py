
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

# Marcus on bass: walking line, D2-G2 (MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (MIDI 38), F2 (MIDI 41), D2 (MIDI 38), Eb2 (MIDI 39)
    (38, 1.5), (41, 1.875), (38, 2.25), (39, 2.625),
    # Bar 3: G2 (MIDI 43), Bb2 (MIDI 42), G2 (MIDI 43), A2 (MIDI 45)
    (43, 2.875), (42, 3.25), (43, 3.625), (45, 4.0),
    # Bar 4: D2 (MIDI 38), F2 (MIDI 41), D2 (MIDI 38), Eb2 (MIDI 39)
    (38, 4.25), (41, 4.625), (38, 5.0), (39, 5.375)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Diane on piano: Open voicings, resolve on the last chord of each bar
# Bar 2: Dm7 (C, D, F, G)
piano_notes_bar2 = [(60, 1.5), (62, 1.5), (65, 1.5), (67, 1.5)]
# Bar 3: G7 (F#, G, B, D)
piano_notes_bar3 = [(66, 2.875), (67, 2.875), (71, 2.875), (69, 2.875)]
# Bar 4: Cm7 (Bb, C, Eb, F)
piano_notes_bar4 = [(59, 4.25), (60, 4.25), (63, 4.25), (65, 4.25)]
for note, time in piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.75))

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (MIDI 62), F (65), Eb (64), D (62)
# Play on beat 1 of bar 2, then leave it hanging, return on beat 3 of bar 4
sax_notes = [
    (62, 1.5), (65, 1.875), (64, 2.25), (62, 2.625),
    (62, 4.625), (65, 4.875), (64, 5.125), (62, 5.375)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
