
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375),
    (36, 0.75, 0.375), (38, 1.125, 0.375),
    # Hihat on every eighth
    (42, 0.0, 0.1875), (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875),
    (42, 1.125, 0.1875), (42, 1.3125, 0.1875),
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4 (1.5 - 6.0s)
# Start with sax on bar 2

# Sax melody
# D (D4), F#, A, B (Dorian mode), with rests and dynamic shifts
sax_notes = [
    # Bar 2
    (62, 1.5, 0.375),  # D4
    (67, 2.25, 0.375), # F#4
    (69, 3.0, 0.375),  # A4
    (71, 3.75, 0.375), # B4
    (69, 4.5, 0.375),  # A4
    # Bar 3
    (62, 5.25, 0.375), # D4
    (67, 6.0, 0.375),  # F#4
    (69, 6.75, 0.375), # A4
    # Bar 4
    (71, 7.5, 0.375),  # B4
    (69, 8.25, 0.375), # A4
    (67, 9.0, 0.375),  # F#4
    (62, 9.75, 0.375), # D4
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bass line: walking line in D Dorian
bass_notes = [
    # Bar 2
    (45, 1.5, 0.375),  # D3
    (47, 1.875, 0.375), # E3
    (45, 2.25, 0.375),  # D3
    (44, 2.625, 0.375), # C3
    # Bar 3
    (46, 3.0, 0.375),  # D#3
    (45, 3.375, 0.375), # D3
    (47, 3.75, 0.375),  # E3
    (49, 4.125, 0.375), # F#3
    # Bar 4
    (47, 4.5, 0.375),  # E3
    (45, 4.875, 0.375), # D3
    (44, 5.25, 0.375),  # C3
    (46, 5.625, 0.375), # D#3
    (47, 6.0, 0.375),  # E3
    (49, 6.375, 0.375), # F#3
    (47, 6.75, 0.375),  # E3
    (45, 7.125, 0.375), # D3
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
# Bar 2: D7 on beat 2
piano_notes = [
    # Bar 2
    (62, 2.25, 0.375),  # D4
    (67, 2.25, 0.375),  # F#4
    (69, 2.25, 0.375),  # A4
    (71, 2.25, 0.375),  # B4
    # Bar 3: D7 on beat 2
    (62, 3.75, 0.375),  # D4
    (67, 3.75, 0.375),  # F#4
    (69, 3.75, 0.375),  # A4
    (71, 3.75, 0.375),  # B4
    # Bar 4: D7 on beat 2
    (62, 5.25, 0.375),  # D4
    (67, 5.25, 0.375),  # F#4
    (69, 5.25, 0.375),  # A4
    (71, 5.25, 0.375),  # B4
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick
    drum_notes.append((36, bar_start, 0.375))
    drum_notes.append((36, bar_start + 0.75, 0.375))
    # Snare
    drum_notes.append((38, bar_start + 0.375, 0.375))
    drum_notes.append((38, bar_start + 1.125, 0.375))
    # Hihat
    for i in range(8):
        drum_notes.append((42, bar_start + i * 0.1875, 0.1875))

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
