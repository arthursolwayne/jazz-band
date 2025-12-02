
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
bar_length = 1.5
drum_notes = [
    (0.0, 36, 100),   # Kick on 1
    (0.375, 42, 100), # Hihat on 2
    (0.75, 38, 100),  # Snare on 3
    (1.125, 42, 100), # Hihat on 4
    (1.5, 36, 100)    # Kick on 1 of next bar
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43)
bass_notes = [
    (1.5, 43, 100),   # G2
    (1.875, 41, 100), # F2
    (2.25, 40, 100),  # E2
    (2.625, 38, 100), # D2
    (3.0, 43, 100),   # G2
    (3.375, 41, 100), # F2
    (3.75, 40, 100),  # E2
    (4.125, 38, 100), # D2
    (4.5, 43, 100),   # G2
    (4.875, 41, 100), # F2
    (5.25, 40, 100),  # E2
    (5.625, 38, 100)  # D2
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Diane: Open voicings, different chord each bar, resolve on the last.
piano_notes = [
    # Bar 2: Dm7 (F, A, D, G)
    (1.5, 62, 100), (1.5, 65, 100), (1.5, 67, 100), (1.5, 69, 100),
    # Bar 3: G7 (B, D, G, B)
    (3.0, 71, 100), (3.0, 67, 100), (3.0, 69, 100), (3.0, 71, 100),
    # Bar 4: Cm7 (E, G, C, E)
    (4.5, 64, 100), (4.5, 67, 100), (4.5, 60, 100), (4.5, 64, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * bar_length
    # Kick on 1
    drums.notes.append(pretty_midi.Note(100, 36, start, start + 0.125))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(100, 38, start + 0.375, start + 0.375 + 0.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(100, 36, start + 0.75, start + 0.75 + 0.125))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(100, 38, start + 1.125, start + 1.125 + 0.125))
    # Hihat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(100, 42, start + i * 0.125, start + i * 0.125 + 0.125))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    (1.5, 65, 100), (1.5, 60, 100), (1.5, 62, 100), (1.5, 65, 100),
    # Bar 3: Leave it hanging
    (3.0, 62, 100), (3.0, 60, 100), (3.0, 62, 100), (3.0, 62, 100),
    # Bar 4: Come back and finish it
    (4.5, 65, 100), (4.5, 60, 100), (4.5, 62, 100), (4.5, 65, 100)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
