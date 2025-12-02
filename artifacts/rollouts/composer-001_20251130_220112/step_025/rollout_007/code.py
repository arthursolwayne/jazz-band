
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
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Start of sax melody
bar_start = 1.5
bar_duration = 1.5

# Sax melody (Dante)
# F7 -> G7 -> A7 -> Bb7 (F major)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=89, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=91, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=88, start=bar_start + 1.125, end=bar_start + 1.5)
]
sax.notes.extend(sax_notes)

# Bass line (Marcus) - walking line with chromatic approaches
# F -> G -> A -> Bb -> C -> D -> Eb -> F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=55, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=57, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=59, start=bar_start + 1.125, end=bar_start + 1.5)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
# F7 on beat 2, Bb7 on beat 4
piano_notes = []
# F7 (F, A, C, Eb) on beat 2 (bar_start + 0.375)
for pitch in [53, 58, 60, 62]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar_start + 0.375, end=bar_start + 0.75))
# Bb7 (Bb, D, F, Ab) on beat 4 (bar_start + 1.125)
for pitch in [59, 64, 66, 68]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar_start + 1.125, end=bar_start + 1.5))
piano.notes.extend(piano_notes)

# Bar 3: Full quartet
bar_start = 3.0
# Sax melody (Dante) continues with a variation
# G7 -> A7 -> Bb7 -> C7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=89, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=91, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=93, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=96, start=bar_start + 1.125, end=bar_start + 1.5)
]
sax.notes.extend(sax_notes)

# Bass line (Marcus) - walking line with chromatic approaches
# F -> G -> A -> Bb -> C -> D -> Eb -> F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=55, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=57, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=59, start=bar_start + 1.125, end=bar_start + 1.5)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
# G7 on beat 2, C7 on beat 4
piano_notes = []
# G7 (G, B, D, F) on beat 2 (bar_start + 0.375)
for pitch in [55, 58, 62, 65]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar_start + 0.375, end=bar_start + 0.75))
# C7 (C, E, G, Bb) on beat 4 (bar_start + 1.125)
for pitch in [60, 64, 67, 68]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar_start + 1.125, end=bar_start + 1.5))
piano.notes.extend(piano_notes)

# Drums (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3]:
    start = bar_start + (bar - 2) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bar 4: Full quartet
bar_start = 4.5
# Sax melody (Dante) - return to the original motif and finish it
# F7 -> G7 -> A7 -> Bb7 (F major)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=89, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=91, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=88, start=bar_start + 1.125, end=bar_start + 1.5)
]
sax.notes.extend(sax_notes)

# Bass line (Marcus) - walking line with chromatic approaches
# F -> G -> A -> Bb -> C -> D -> Eb -> F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=55, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=57, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=59, start=bar_start + 1.125, end=bar_start + 1.5)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
# F7 on beat 2, Bb7 on beat 4
piano_notes = []
# F7 (F, A, C, Eb) on beat 2 (bar_start + 0.375)
for pitch in [53, 58, 60, 62]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar_start + 0.375, end=bar_start + 0.75))
# Bb7 (Bb, D, F, Ab) on beat 4 (bar_start + 1.125)
for pitch in [59, 64, 66, 68]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar_start + 1.125, end=bar_start + 1.5))
piano.notes.extend(piano_notes)

# Drums (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
start = bar_start
# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
# Hihat on every eighth
hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
