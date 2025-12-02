
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
    (36, 0.0, 1.0),   # Kick on beat 1
    (42, 0.0, 1.0),   # Hihat on beat 1
    (38, 0.5, 1.0),   # Snare on beat 2
    (42, 0.5, 1.0),   # Hihat on beat 2
    (36, 1.0, 1.0),   # Kick on beat 3
    (42, 1.0, 1.0),   # Hihat on beat 3
    (38, 1.5, 1.0),   # Snare on beat 4
    (42, 1.5, 1.0),   # Hihat on beat 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (62, 1.5, 0.25),  # D
    (63, 1.75, 0.25), # Eb
    (64, 2.0, 0.25),  # E
    (62, 2.25, 0.25), # D
    (60, 2.5, 0.25),  # C
    (62, 2.75, 0.25), # D
    (63, 3.0, 0.25),  # Eb
    (64, 3.25, 0.25), # E
    (65, 3.5, 0.25),  # F
    (67, 3.75, 0.25), # G
    (69, 4.0, 0.25),  # A
    (67, 4.25, 0.25), # G
    (65, 4.5, 0.25),  # F
    (64, 4.75, 0.25), # E
    (62, 5.0, 0.25),  # D
    (60, 5.25, 0.25), # C
    (62, 5.5, 0.25),  # D
    (63, 5.75, 0.25), # Eb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 2.0, 0.25),  # D7 (62, 64, 67, 71)
    (64, 2.0, 0.25),
    (67, 2.0, 0.25),
    (71, 2.0, 0.25),
    (62, 4.0, 0.25),
    (64, 4.0, 0.25),
    (67, 4.0, 0.25),
    (71, 4.0, 0.25),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on beat 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.5)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.0, end=bar_start + 1.5)
    # Snare on beat 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.5, end=bar_start + 1.0)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 2.0)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.5)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.5, end=bar_start + 1.0)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.0, end=bar_start + 1.5)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 2.0)
    # Add to drums
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.3),   # D
    (63, 1.8, 0.3),   # Eb
    (64, 2.1, 0.3),   # E
    (62, 2.4, 0.3),   # D
    (65, 3.0, 0.3),   # F
    (64, 3.3, 0.3),   # E
    (62, 3.6, 0.3),   # D
    (60, 3.9, 0.3),   # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
