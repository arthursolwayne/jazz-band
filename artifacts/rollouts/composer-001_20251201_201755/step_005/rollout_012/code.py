
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.125, 0.25), # Hihat on & 2
    (38, 0.375, 0.375), # Snare on 3
    (42, 0.5, 0.25),   # Hihat on & 4
    (36, 0.75, 0.375), # Kick on 1
    (42, 0.875, 0.25), # Hihat on & 2
    (38, 1.125, 0.375),# Snare on 3
    (42, 1.25, 0.25)   # Hihat on & 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (D2, F#2, A2, C#3) walking line with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375), # D2 on 1
    (40, 1.875, 0.375), # F#2 on 3
    (43, 2.25, 0.375), # A2 on 1
    (45, 2.625, 0.375), # C#3 on 3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D, F#, A, C#)
piano_notes = [
    (55, 1.5, 0.375), # D
    (60, 1.5, 0.375), # F#
    (64, 1.5, 0.375), # A
    (67, 1.5, 0.375), # C#
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Start the motif
sax_notes = [
    (62, 1.5, 0.375), # E
    (65, 1.875, 0.375), # G
    (62, 2.25, 0.375), # E
    (65, 2.625, 0.375) # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F#2 (D2, F#2, A2, C#3) walking line with chromatic approaches
bass_notes = [
    (40, 3.0, 0.375), # F#2 on 1
    (43, 3.375, 0.375), # A2 on 3
    (45, 3.75, 0.375), # C#3 on 1
    (47, 4.125, 0.375), # E3 on 3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: D7 (D, F#, A, C)
piano_notes = [
    (55, 3.0, 0.375), # D
    (60, 3.0, 0.375), # F#
    (64, 3.0, 0.375), # A
    (60, 3.375, 0.375), # C on 3
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Continue the motif
sax_notes = [
    (62, 3.0, 0.375), # E
    (65, 3.375, 0.375), # G
    (62, 3.75, 0.375), # E
    (65, 4.125, 0.375) # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: A2 (D2, F#2, A2, C#3) walking line with chromatic approaches
bass_notes = [
    (43, 4.5, 0.375), # A2 on 1
    (47, 4.875, 0.375), # E3 on 3
    (50, 5.25, 0.375), # G3 on 1
    (53, 5.625, 0.375), # Bb3 on 3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Dmaj7 (D, F#, A, C#)
piano_notes = [
    (55, 4.5, 0.375), # D
    (60, 4.5, 0.375), # F#
    (64, 4.5, 0.375), # A
    (67, 4.875, 0.375), # C# on 3
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Finish the motif
sax_notes = [
    (62, 4.5, 0.375), # E
    (65, 4.875, 0.375), # G
    (67, 5.25, 0.375), # A
    (65, 5.625, 0.375) # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Fill the bar
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.625, 0.25), # Hihat on & 2
    (38, 4.875, 0.375),# Snare on 3
    (42, 5.0, 0.25),   # Hihat on & 4
    (36, 5.25, 0.375), # Kick on 1
    (42, 5.375, 0.25), # Hihat on & 2
    (38, 5.625, 0.375),# Snare on 3
    (42, 5.75, 0.25)   # Hihat on & 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
