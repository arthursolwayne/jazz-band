
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),  # Kick on beat 1
    (42, 0.0, 0.1875), # Hihat on 1& (half of 1/8)
    (42, 0.1875, 0.1875), # Hihat on 2& (half of 1/8)
    (42, 0.375, 0.1875), # Hihat on 3& (half of 1/8)
    (42, 0.5625, 0.1875), # Hihat on 4& (half of 1/8)
    (38, 0.75, 0.375),  # Snare on beat 2
    (36, 1.125, 0.375), # Kick on beat 3
    (42, 1.125, 0.1875), # Hihat on 3& (half of 1/8)
    (42, 1.3125, 0.1875), # Hihat on 4& (half of 1/8)
    (38, 1.5, 0.375)    # Snare on beat 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus - Bass
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375), # Eb (chromatic approach)
    (62, 2.25, 0.375),  # D
    (61, 2.625, 0.375)  # C (chromatic approach)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane - Piano
piano_notes = [
    (67, 1.5, 0.375),  # B7 (D7 chord)
    (64, 1.875, 0.375),  # E7
    (65, 2.25, 0.375),  # F#7
    (62, 2.625, 0.375)  # A7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Dante - Sax
sax_notes = [
    (62, 1.5, 0.375),  # D (start of motif)
    (64, 1.875, 0.375),  # E (second note of motif)
    (62, 2.25, 0.375),  # D (third note of motif)
    (60, 2.625, 0.375)  # C (ending note, hanging)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus - Bass
bass_notes = [
    (64, 3.0, 0.375),  # Eb
    (65, 3.375, 0.375), # F#
    (67, 3.75, 0.375),  # A
    (64, 4.125, 0.375)  # Eb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane - Piano
piano_notes = [
    (69, 3.0, 0.375),  # D7 (D7 chord)
    (66, 3.375, 0.375),  # G7
    (68, 3.75, 0.375),  # A7
    (64, 4.125, 0.375)  # E7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Dante - Sax
sax_notes = [
    (62, 3.0, 0.375),  # D (repeat motif)
    (64, 3.375, 0.375),  # E
    (62, 3.75, 0.375),  # D
    (60, 4.125, 0.375)  # C (ending note, hanging)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus - Bass
bass_notes = [
    (62, 4.5, 0.375),  # D
    (63, 4.875, 0.375), # Eb
    (62, 5.25, 0.375),  # D
    (61, 5.625, 0.375)  # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane - Piano
piano_notes = [
    (67, 4.5, 0.375),  # B7 (D7 chord)
    (64, 4.875, 0.375),  # E7
    (65, 5.25, 0.375),  # F#7
    (62, 5.625, 0.375)  # A7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Dante - Sax
sax_notes = [
    (62, 4.5, 0.375),  # D (repeat motif)
    (64, 4.875, 0.375),  # E
    (62, 5.25, 0.375),  # D
    (60, 5.625, 0.375)  # C (ending note, resolve)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums continue with same pattern
bar3_start = 3.0
bar4_start = 4.5

# Bar 3
for note, start, duration in drum_notes:
    new_start = bar3_start + start
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=new_start, end=new_start + duration))

# Bar 4
for note, start, duration in drum_notes:
    new_start = bar4_start + start
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=new_start, end=new_start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
