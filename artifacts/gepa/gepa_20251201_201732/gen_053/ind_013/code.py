
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
    (36, 0.0),     # kick on 1
    (38, 0.375),   # snare on 2
    (36, 0.75),    # kick on 3
    (38, 1.125),   # snare on 4
    (42, 0.0),     # hihat on 1
    (42, 0.125),
    (42, 0.25),
    (42, 0.375),
    (42, 0.5),
    (42, 0.625),
    (42, 0.75),
    (42, 0.875),
    (42, 1.0),
    (42, 1.125),
    (42, 1.25),
    (42, 1.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5),   # D2
    (40, 1.875), # F2 (chromatic approach)
    (43, 2.25),  # G2
    (41, 2.625), # F#2 (chromatic approach)
    (38, 3.0),   # D2
    (40, 3.375), # F2
    (43, 3.75),  # G2
    (41, 4.125), # F#2
    (38, 4.5),   # D2
    (40, 4.875), # F2
    (43, 5.25),  # G2
    (41, 5.625)  # F#2
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
# Bar 3: G7 (G, B, D, F)
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    (50, 1.5), # D
    (53, 1.5), # F
    (57, 1.5), # A
    (60, 1.5), # C
    # Bar 3 (2.25 - 3.0s)
    (62, 2.25), # G
    (67, 2.25), # B
    (67, 2.625), # D (octave)
    (65, 2.25), # F
    # Bar 4 (3.0 - 3.75s)
    (60, 3.0), # C
    (63, 3.0), # Eb
    (67, 3.0), # G
    (71, 3.0), # Bb
    # Resolutions
    (57, 3.75), # A
    (60, 3.75), # C
    (64, 3.75), # D (octave)
    (67, 3.75)  # F (octave)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# You: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (50), F (53), E (52), rest
sax_notes = [
    (50, 1.5),  # D
    (53, 1.875), # F
    (52, 2.25),  # E
    (50, 3.0),   # D
    (53, 3.375), # F
    (52, 3.75)   # E
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
