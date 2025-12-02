
import pretty_midi

# Initialize the MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time in seconds per bar at 160 BPM
BAR_DURATION = 1.5  # 60 / 160 * 4 = 1.5 seconds

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

bar_1_start = 0.0
bar_1_end = bar_1_start + BAR_DURATION

# Kick on beats 1 and 3 (0.0 and 0.75s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=bar_1_start, end=bar_1_start + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=bar_1_start + 0.75, end=bar_1_start + 0.85))

# Snare on 2 and 4 (0.375 and 1.125s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=bar_1_start + 0.375, end=bar_1_start + 0.475))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=bar_1_start + 1.125, end=bar_1_start + 1.225))

# Hi-hat on every eighth note
for i in range(8):
    start = bar_1_start + i * 0.375
    end = start + 0.1
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=start, end=end))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus) - walking line in D with chromatic approaches
# We'll use a D Dorian scale with chromatic passing tones

# Dorian scale in D: D, E, F#, G, A, B, C
# Chromatic passing tones: E#, C#, etc.

# Bass line (1.5s to 6.0s)
bass_notes = [
    # Bar 2: D (1.5s) -> C# chromatic (1.5s) -> D (1.75s) -> E (2.0s)
    (1.5, 62),  # D (MIDI 62)
    (1.5, 63),  # C# (chromatic)
    (1.75, 62),  # D
    (2.0, 64),  # E
    # Bar 3: F# (2.25s) -> G (2.5s) -> A (2.75s) -> B (3.0s)
    (2.25, 66),  # F#
    (2.5, 67),  # G
    (2.75, 69),  # A
    (3.0, 71),  # B
    # Bar 4: C (3.25s) -> D (3.5s) -> E (3.75s) -> F# (4.0s)
    (3.25, 60),  # C
    (3.5, 62),  # D
    (3.75, 64),  # E
    (4.0, 66),  # F#
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25))

# Piano (Diane) - 7th chords on 2 and 4
# D7: D, F#, A, C
# G7: G, B, D, F
# B7: B, D#, F#, A
# F#7: F#, A, C, E

piano_notes = [
    # Bar 2: D7 on beat 2 (1.875s) and 4 (2.625s)
    (1.875, 62), (1.875, 66), (1.875, 69), (1.875, 60),
    (2.625, 62), (2.625, 66), (2.625, 69), (2.625, 60),
    # Bar 3: G7 on beat 2 (3.125s) and 4 (3.875s)
    (3.125, 67), (3.125, 71), (3.125, 62), (3.125, 64),
    (3.875, 67), (3.875, 71), (3.875, 62), (3.875, 64),
    # Bar 4: B7 on beat 2 (4.375s) and 4 (5.125s)
    (4.375, 71), (4.375, 74), (4.375, 66), (4.375, 69),
    (5.125, 71), (5.125, 74), (5.125, 66), (5.125, 69),
]

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=pitch, start=start, end=start + 0.1))

# Drums: continuation of the same pattern for Bars 2-4
for bar in range(2, 5):
    bar_start = bar * BAR_DURATION
    bar_end = bar_start + BAR_DURATION

    # Kick on 1 and 3 (0.0 and 0.75s relative to bar start)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=bar_start, end=bar_start + 0.1))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=bar_start + 0.75, end=bar_start + 0.85))

    # Snare on 2 and 4 (0.375 and 1.125s relative to bar start)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=bar_start + 0.375, end=bar_start + 0.475))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=bar_start + 1.125, end=bar_start + 1.225))

    # Hi-hat on every eighth note (0.0, 0.375, 0.75, ..., up to 1.5s)
    for i in range(8):
        start = bar_start + i * 0.375
        end = start + 0.1
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=start, end=end))

# Sax (Dante) - short motif in D, starting at 1.5s
# D, F#, A, D (1.5s - 2.0s)
sax_notes = [
    (1.5, 62),  # D
    (1.75, 66),  # F#
    (2.0, 69),  # A
    (2.25, 62),  # D
    (2.5, 62),  # D again (hang)
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=start + 0.25))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
