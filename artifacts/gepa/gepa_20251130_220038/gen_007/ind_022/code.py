
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
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on 2
    (1.25, 38, 100), # Snare on 3
    (1.5, 42, 100)   # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    (1.5, 62, 100),  # D4
    (1.75, 63, 100), # Eb4
    (2.0, 65, 100),  # F#4
    (2.25, 67, 100), # A4
    (2.5, 69, 100),  # B4
    (2.75, 71, 100), # C#5
    (3.0, 72, 100),  # D5
    (3.25, 71, 100), # C#5
    (3.5, 69, 100),  # B4
    (3.75, 67, 100), # A4
    (4.0, 65, 100),  # F#4
    (4.25, 63, 100), # Eb4
    (4.5, 62, 100),  # D4
    (4.75, 60, 100), # C4
    (5.0, 62, 100),  # D4
    (5.25, 64, 100), # E4
    (5.5, 66, 100),  # F#4
    (5.75, 69, 100)  # B4
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.75, 67, 100), # A4
    (1.75, 71, 100), # C#5
    (1.75, 72, 100), # D5
    (1.75, 76, 100), # F#5
    # Bar 3
    (3.25, 67, 100),
    (3.25, 71, 100),
    (3.25, 72, 100),
    (3.25, 76, 100),
    # Bar 4
    (4.75, 67, 100),
    (4.75, 71, 100),
    (4.75, 72, 100),
    (4.75, 76, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(100, 36, bar_start, bar_start + 0.125))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(100, 38, bar_start + 0.75, bar_start + 0.875))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(100, 36, bar_start + 1.25, bar_start + 1.375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(100, 38, bar_start + 1.5, bar_start + 1.625))
    # Hihat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(100, 42, bar_start + i * 0.125, bar_start + i * 0.125 + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 71, 100),  # C#5
    (1.666, 69, 100), # B4
    (1.833, 67, 100), # A4
    (2.0, 69, 100),  # B4
    (2.166, 71, 100), # C#5
    (2.333, 72, 100), # D5
    (2.5, 69, 100),  # B4
    (2.666, 67, 100), # A4
    (2.833, 64, 100), # E4
    (3.0, 62, 100),  # D4
    (3.166, 64, 100), # E4
    (3.333, 67, 100), # A4
    (3.5, 69, 100),  # B4
    (3.666, 71, 100), # C#5
    (3.833, 72, 100), # D5
    (4.0, 69, 100),  # B4
    (4.166, 67, 100), # A4
    (4.333, 64, 100), # E4
    (4.5, 62, 100),  # D4
    (4.666, 64, 100), # E4
    (4.833, 67, 100), # A4
    (5.0, 69, 100),  # B4
    (5.166, 71, 100), # C#5
    (5.333, 72, 100), # D5
    (5.5, 69, 100),  # B4
    (5.666, 67, 100), # A4
    (5.833, 64, 100), # E4
    (6.0, 62, 100)   # D4
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
