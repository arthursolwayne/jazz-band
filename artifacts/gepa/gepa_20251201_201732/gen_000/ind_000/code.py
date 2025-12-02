
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
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Everyone in. Start of the melody with sax.
# Sax: Fm7 -> Bb7 -> Eb7 -> Ab7
# Melody: F, Ab, Bb, D
# Start with F, leave it hanging
sax_note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75)
sax.notes.append(sax_note)

# Bass: Walking line in Fm (F, G, Ab, A)
bass_notes = [
    (71, 1.5, 0.375),  # F
    (72, 1.875, 0.375), # G
    (70, 2.25, 0.375),  # Ab
    (71, 2.625, 0.375)  # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    (71, 1.5, 0.375),  # F
    (70, 1.5, 0.375),  # Ab
    (74, 1.5, 0.375),  # C
    (69, 1.5, 0.375)   # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    (73, 2.25, 0.375),  # Bb
    (76, 2.25, 0.375),  # D
    (71, 2.25, 0.375),  # F
    (70, 2.25, 0.375)   # Ab
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes = [
    (69, 3.0, 0.375),  # Eb
    (74, 3.0, 0.375),  # G
    (73, 3.0, 0.375),  # Bb
    (76, 3.0, 0.375)   # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums continue in Bar 2-4 with same pattern
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.375),  # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.375), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.375), # Hihat on 4

    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.375),  # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.375), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Finish the motif on D in bar 4
sax_note = pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.375)
sax.notes.append(sax_note)

# Bass: End with Ab on beat 4
bass_notes = [
    (70, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: End with D on beat 4
piano_notes = [
    (76, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
