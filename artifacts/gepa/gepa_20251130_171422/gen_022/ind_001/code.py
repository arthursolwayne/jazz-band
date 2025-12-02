
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth
hihat_time = 0.0
while hihat_time < 1.5:
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_time, end=hihat_time + 0.125))
    hihat_time += 0.125

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
# Walking line with chromatic approaches
bass_notes = [
    (1.5, 62, 100),  # D3
    (1.75, 63, 100),  # Eb3
    (2.0, 64, 100),  # E3
    (2.25, 62, 100),  # D3
    (2.5, 60, 100),  # C3
    (2.75, 62, 100),  # D3
    (3.0, 64, 100),  # E3
    (3.25, 65, 100),  # F3
    (3.5, 67, 100),  # G3
    (3.75, 65, 100),  # F3
    (4.0, 64, 100),  # E3
    (4.25, 62, 100),  # D3
    (4.5, 60, 100),  # C3
    (4.75, 59, 100),  # B2
    (5.0, 60, 100),  # C3
    (5.25, 62, 100),  # D3
    (5.5, 64, 100),  # E3
    (5.75, 65, 100),  # F3
]
for start, pitch, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25))

# Piano: Diane
# 7th chords on 2 and 4, sparse comp
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    (2.0, 62, 90),  # D3
    (2.0, 67, 90),  # A3
    (2.0, 64, 90),  # E3
    (2.0, 69, 90),  # C4

    # Bar 3: Bm7 (B, D, F#, A)
    (3.5, 69, 90),  # B3
    (3.5, 62, 90),  # D3
    (3.5, 67, 90),  # F#3
    (3.5, 69, 90),  # A3

    # Bar 4: D7 again
    (5.0, 62, 90),  # D3
    (5.0, 67, 90),  # A3
    (5.0, 64, 90),  # E3
    (5.0, 69, 90),  # C4
]
for start, pitch, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 * bar
    # Kick
    midi_time = bar_start
    kick = pretty_midi.Note(velocity=100, pitch=36, start=midi_time, end=midi_time + 0.375)
    drums.notes.append(kick)
    midi_time += 1.125
    kick = pretty_midi.Note(velocity=100, pitch=36, start=midi_time, end=midi_time + 0.375)
    drums.notes.append(kick)

    # Snare
    midi_time = bar_start + 0.75
    snare = pretty_midi.Note(velocity=110, pitch=38, start=midi_time, end=midi_time + 0.125)
    drums.notes.append(snare)
    midi_time = bar_start + 1.875
    snare = pretty_midi.Note(velocity=110, pitch=38, start=midi_time, end=midi_time + 0.125)
    drums.notes.append(snare)

    # Hihat
    hihat_time = bar_start
    while hihat_time < bar_start + 1.5:
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_time, end=hihat_time + 0.125)
        drums.notes.append(hihat)
        hihat_time += 0.125

# Sax: Dante - sparse melody
# Motif: D, F#, Bb, D (Dorian)
sax_notes = [
    # Bar 2
    (2.0, 62, 100),  # D3
    (2.25, 67, 100),  # F#3
    (2.5, 60, 100),  # Bb3
    (2.75, 62, 100),  # D3

    # Bar 3
    (3.0, 60, 100),  # Bb3
    (3.25, 62, 90),  # D3
    (3.5, 67, 95),  # F#3
    (3.75, 71, 95),  # A3

    # Bar 4
    (4.0, 69, 110),  # B3
    (4.25, 67, 100),  # F#3
    (4.5, 64, 100),  # E3
    (4.75, 62, 110),  # D3

    # End note
    (5.0, 62, 110),  # D3
    (5.25, 62, 70),  # D3 (fade out)
    (5.5, 62, 50),  # D3 (fade out)
]
for start, pitch, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
