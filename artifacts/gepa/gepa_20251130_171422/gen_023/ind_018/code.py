
import pretty_midi

# Create a MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for each musician
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define MIDI note numbers
# Dm7: D (62), F (64), A (69), C (60)
# Chromatic bass line
# Drums: kick (36), snare (38), hihat (42)

# Bar 1: Little Ray (Drums) alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4])

# Bar 2: Full quartet begins (1.5 - 3.0s)
# Sax: Start of the melody motif
# Dm7 chord: D (62), F (64), A (69), C (60)
# Motif: D (62) -> F (64) -> C (60) -> D (62) -> Bb (61) -> A (69)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),   # D
    pretty_midi.Note(velocity=100, pitch=61, start=2.5, end=2.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),   # A
]
sax.notes.extend(sax_notes)

# Bass: Chromatic walking line
# Start from D (62), walk down chromatically
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),   # C
    pretty_midi.Note(velocity=80, pitch=60, start=2.0, end=2.25),   # B
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.5),   # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=2.5, end=2.75),   # B
    pretty_midi.Note(velocity=80, pitch=61, start=2.75, end=3.0),   # C
]
bass.notes.extend(bass_notes)

# Piano: Dm7 on 2 and 4
# Chord: D (62), F (64), A (69), C (60)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),   # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),   # A
    pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=3.0),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),   # A
]
piano.notes.extend(piano_notes)

# Drums continue the same pattern (1.5 - 3.0s)
for bar in range(1):
    start = 1.5 + bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif, but start on Bb (61)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=100, pitch=61, start=4.0, end=4.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),   # A
]
sax.notes.extend(sax_notes)

# Bass: Continue chromatic line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.25),   # A
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),   # G
    pretty_midi.Note(velocity=80, pitch=66, start=3.5, end=3.75),   # F
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.0),   # E
    pretty_midi.Note(velocity=80, pitch=66, start=4.0, end=4.25),   # F
    pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.5),   # G
]
bass.notes.extend(bass_notes)

# Piano: Dm7 on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),   # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),   # A
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.5),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.5),   # A
]
piano.notes.extend(piano_notes)

# Drums continue the same pattern (3.0 - 4.5s)
for bar in range(1):
    start = 3.0 + bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Melody motif ends with a resolution to the 5th (A) of the Dm7 chord
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),   # A
]
sax.notes.extend(sax_notes)

# Bass: Chromatic line resolves back up
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75),   # E
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),   # F
    pretty_midi.Note(velocity=80, pitch=66, start=5.0, end=5.25),   # G
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5),   # A
    pretty_midi.Note(velocity=80, pitch=68, start=5.5, end=5.75),   # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=5.75, end=6.0),   # B
]
bass.notes.extend(bass_notes)

# Piano: Dm7 on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),   # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),   # A
    pretty_midi.Note(velocity=90, pitch=60, start=5.75, end=6.0),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0),   # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.75, end=6.0),   # A
]
piano.notes.extend(piano_notes)

# Drums continue the same pattern (4.5 - 6.0s)
for bar in range(1):
    start = 4.5 + bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4])

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
