
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
drum_notes = [
    (0.0, 36, 100),   # Kick on 1
    (0.75, 42, 100),  # Hihat on 2
    (1.25, 38, 100),  # Snare on 3
    (1.5, 42, 100)    # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Dm (F, Ab, D, C)
bass_notes = [
    (1.5, 65, 100),   # F (Dm root)
    (2.0, 63, 100),   # Ab (Dm b7)
    (2.5, 67, 100),   # D (Dm 5)
    (3.0, 64, 100),   # C (Dm b3)
    (3.5, 65, 100),   # F
    (4.0, 63, 100),   # Ab
    (4.5, 67, 100),   # D
    (5.0, 64, 100),   # C
    (5.5, 65, 100)    # F
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Diane: 7th chords, comp on 2 and 4 (Dm7)
piano_notes = [
    (1.5, 67, 100),   # D (root)
    (1.5, 69, 100),   # F (3)
    (1.5, 70, 100),   # Ab (b7)
    (1.5, 72, 100),   # C (b3)
    (2.0, 67, 100),   # D
    (2.0, 69, 100),   # F
    (2.0, 70, 100),   # Ab
    (2.0, 72, 100),   # C
    (3.0, 67, 100),   # D
    (3.0, 69, 100),   # F
    (3.0, 70, 100),   # Ab
    (3.0, 72, 100),   # C
    (4.0, 67, 100),   # D
    (4.0, 69, 100),   # F
    (4.0, 70, 100),   # Ab
    (4.0, 72, 100)    # C
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth (starting at 1.5s)
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1
    kick_time = bar_start
    drums.notes.append(pretty_midi.Note(100, 36, kick_time, kick_time + 0.125))
    # Snare on 2
    snare_time = bar_start + 0.75
    drums.notes.append(pretty_midi.Note(100, 38, snare_time, snare_time + 0.125))
    # Kick on 3
    kick_time = bar_start + 1.25
    drums.notes.append(pretty_midi.Note(100, 36, kick_time, kick_time + 0.125))
    # Snare on 4
    snare_time = bar_start + 1.5
    drums.notes.append(pretty_midi.Note(100, 38, snare_time, snare_time + 0.125))
    # Hihat on every eighth
    for i in range(8):
        hihat_time = bar_start + i * 0.375
        drums.notes.append(pretty_midi.Note(100, 42, hihat_time, hihat_time + 0.125))

# Dante: Tenor sax melody - short motif, one phrase, leave it hanging
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, Eb, F, C (start), then return with a variation
# Start at 1.5s
sax_notes = [
    (1.5, 67, 100),   # D
    (1.6, 69, 100),   # Eb
    (1.7, 71, 100),   # F
    (1.8, 64, 100),   # C
    (2.0, 67, 100),   # D
    (2.2, 69, 100),   # Eb
    (2.4, 71, 100),   # F
    (2.6, 67, 100),   # D
    (3.0, 67, 100),   # D
    (3.5, 71, 100),   # F
    (4.0, 64, 100),   # C
    (4.5, 67, 100),   # D
    (5.0, 69, 100),   # Eb
    (5.5, 71, 100),   # F
    (6.0, 64, 100)    # C
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
