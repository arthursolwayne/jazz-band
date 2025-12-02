
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42, 42, 42, 42]

# Bar 1 timing: 0.0 to 1.5s
bar1_start = 0.0
bar1_duration = 1.5
bar1_beat = 0.375

# Kicks on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + bar1_beat * 2, end=bar1_start + bar1_beat * 2 + 0.1))

# Snares on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + bar1_beat, end=bar1_start + bar1_beat + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + bar1_beat * 3, end=bar1_start + bar1_beat * 3 + 0.1))

# Hihats on every eighth
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar1_start + i * bar1_beat, end=bar1_start + i * bar1_beat + 0.05))

# Bars 2-4 (1.5 - 6.0s)

# Bass line (Marcus): walking line, chromatic approaches
bass_notes = [
    (60, 1.5), (61, 1.75), (64, 2.0), (62, 2.25),
    (60, 2.5), (61, 2.75), (64, 3.0), (62, 3.25),
    (60, 3.5), (61, 3.75), (64, 4.0), (62, 4.25),
    (60, 4.5), (61, 4.75), (64, 5.0), (62, 5.25)
]

for pitch, start in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Piano (Diane): 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.5), (67, 1.5), (69, 1.5), (71, 1.5),  # C7
    (67, 2.0), (70, 2.0), (72, 2.0), (74, 2.0),  # D7
    # Bar 3
    (64, 2.5), (67, 2.5), (69, 2.5), (71, 2.5),  # C7
    (67, 3.0), (70, 3.0), (72, 3.0), (74, 3.0),  # D7
    # Bar 4
    (64, 3.5), (67, 3.5), (69, 3.5), (71, 3.5),  # C7
    (67, 4.0), (70, 4.0), (72, 4.0), (74, 4.0)   # D7
]

for pitch, start in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_start = 1.5
for bar in range(3):
    # Kicks on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + bar * 1.5, end=bar_start + bar * 1.5 + 0.1))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + bar * 1.5 + 0.75, end=bar_start + bar * 1.5 + 0.75 + 0.1))
    
    # Snares on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + bar * 1.5 + 0.375, end=bar_start + bar * 1.5 + 0.375 + 0.1))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + bar * 1.5 + 1.125, end=bar_start + bar * 1.5 + 1.125 + 0.1))
    
    # Hihats on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + bar * 1.5 + i * 0.375, end=bar_start + bar * 1.5 + i * 0.375 + 0.05))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: C - E - G - Bb (C7), then rest, then repeat
sax_notes = [
    (60, 1.5), (64, 1.625), (67, 1.75), (69, 1.875),
    (60, 3.0), (64, 3.125), (67, 3.25), (69, 3.375)
]

for pitch, start in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write MIDI file
midi.write("dante_intro.mid")
