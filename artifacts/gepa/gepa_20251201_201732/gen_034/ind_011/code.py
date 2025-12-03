
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=bar1_start, end=bar1_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=bar1_start + 1.125, end=bar1_start + 1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=bar1_start + 0.75, end=bar1_start + 0.75 + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=bar1_start + 1.875, end=bar1_start + 1.875 + 0.375))

# Hihat on every eighth
for i in range(8):
    start = bar1_start + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=drum_notes['hihat'], start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)

bar2_start = 1.5
bar2_end = 3.0

# Bass: Walking line in F (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: F - C - B - D
bass_notes = [
    (38, bar2_start, bar2_start + 0.375),  # F2
    (43, bar2_start + 0.375, bar2_start + 0.75),  # C3
    (42, bar2_start + 0.75, bar2_start + 1.125),  # B2
    (40, bar2_start + 1.125, bar2_start + 1.5),  # D3 (chromatic approach)
]
for note, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E), open voicing
piano_notes = [
    (64, bar2_start, bar2_end),  # F4
    (69, bar2_start, bar2_end),  # A4
    (72, bar2_start, bar2_end),  # C5
    (76, bar2_start, bar2_end),  # E5
]
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# Sax: Motif - F (G4), Bb (G3?), F (F4) — short, sing, leave it hanging
sax_notes = [
    (71, bar2_start, bar2_start + 0.5),  # G4 (start of motif)
    (67, bar2_start + 0.5, bar2_start + 0.75),  # F#4 (chromatic approach)
    (71, bar2_start + 0.75, bar2_start + 1.0),  # G4 (return to motif)
    (66, bar2_start + 1.0, bar2_start + 1.0 + 0.1),  # F4 (hanging)
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Bar 3: Full quartet (3.0 - 4.5s)

bar3_start = 3.0
bar3_end = 4.5

# Bass: Walking line - Bb - F - E - G (chromatic approach again)
bass_notes = [
    (41, bar3_start, bar3_start + 0.375),  # Bb2
    (38, bar3_start + 0.375, bar3_start + 0.75),  # F2
    (40, bar3_start + 0.75, bar3_start + 1.125),  # E2
    (43, bar3_start + 1.125, bar3_start + 1.5),  # G3
]
for note, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: Cmaj7 (C E G B), open voicing
piano_notes = [
    (67, bar3_start, bar3_end),  # C4
    (72, bar3_start, bar3_end),  # E4
    (76, bar3_start, bar3_end),  # G4
    (81, bar3_start, bar3_end),  # B4
]
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# Sax: Repeat the motif, finish it
sax_notes = [
    (71, bar3_start, bar3_start + 0.5),  # G4
    (67, bar3_start + 0.5, bar3_start + 0.75),  # F#4
    (71, bar3_start + 0.75, bar3_start + 1.0),  # G4
    (71, bar3_start + 1.0, bar3_start + 1.5),  # G4 (full motif — finish it now)
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Drums: Repeat the same pattern for bar 3
for i in range(8):
    start = bar3_start + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=drum_notes['hihat'], start=start, end=end))

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=bar3_start, end=bar3_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=bar3_start + 1.125, end=bar3_start + 1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=bar3_start + 0.75, end=bar3_start + 0.75 + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=bar3_start + 1.875, end=bar3_start + 1.875 + 0.375))

# Bar 4: Full quartet (4.5 - 6.0s)

bar4_start = 4.5
bar4_end = 6.0

# Bass: Walking line - G - D - C - E
bass_notes = [
    (43, bar4_start, bar4_start + 0.375),  # G2
    (40, bar4_start + 0.375, bar4_start + 0.75),  # D2
    (39, bar4_start + 0.75, bar4_start + 1.125),  # C2
    (42, bar4_start + 1.125, bar4_start + 1.5),  # E2
]
for note, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: E7 (E G# B D), open voicing
piano_notes = [
    (76, bar4_start, bar4_end),  # E4
    (81, bar4_start, bar4_end),  # G#4
    (79, bar4_start, bar4_end),  # B4 (chromatic to G#)
    (72, bar4_start, bar4_end),  # D4
]
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# Sax: Motif again — but this time, end it in a way that echoes the first bar
sax_notes = [
    (71, bar4_start, bar4_start + 0.5),  # G4
    (67, bar4_start + 0.5, bar4_start + 0.75),  # F#4
    (71, bar4_start + 0.75, bar4_start + 1.0),  # G4
    (69, bar4_start + 1.0, bar4_start + 1.5),  # A4 (resolution)
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Drums: Same pattern
for i in range(8):
    start = bar4_start + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=drum_notes['hihat'], start=start, end=end))

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=bar4_start, end=bar4_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=bar4_start + 1.125, end=bar4_start + 1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=bar4_start + 0.75, end=bar4_start + 0.75 + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=bar4_start + 1.875, end=bar4_start + 1.875 + 0.375))

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
