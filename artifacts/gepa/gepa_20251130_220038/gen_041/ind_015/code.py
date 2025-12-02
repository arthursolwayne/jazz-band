
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
    (36, 0.0, 0.375),   # Kick on beat 1
    (42, 0.375, 0.375), # Hihat on &1
    (38, 0.75, 0.375),  # Snare on beat 2
    (42, 0.75, 0.375),  # Hihat on &2
    (36, 1.125, 0.375), # Kick on beat 3
    (42, 1.125, 0.375), # Hihat on &3
    (38, 1.5, 0.375),   # Snare on beat 4
    (42, 1.5, 0.375)    # Hihat on &4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm
bass_notes = [
    (35, 1.5, 0.375),   # Bb (Fm root 3rd)
    (31, 1.875, 0.375), # D (chromatic approach)
    (33, 2.25, 0.375),  # E (Fm 7th)
    (30, 2.625, 0.375), # C (Fm 5th)
    (35, 3.0, 0.375),   # Bb
    (31, 3.375, 0.375), # D
    (33, 3.75, 0.375),  # E
    (30, 4.125, 0.375), # C
    (35, 4.5, 0.375),   # Bb
    (31, 4.875, 0.375), # D
    (33, 5.25, 0.375),  # E
    (30, 5.625, 0.375)  # C
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: Piano comping on 2 and 4 with 7th chords
piano_notes = [
    (61, 1.875, 0.375),  # F7 (F, A, C, E♭)
    (65, 1.875, 0.375),
    (60, 1.875, 0.375),
    (63, 1.875, 0.375),
    (61, 3.375, 0.375),  # F7 again
    (65, 3.375, 0.375),
    (60, 3.375, 0.375),
    (63, 3.375, 0.375),
    (61, 4.875, 0.375),  # F7 last time
    (65, 4.875, 0.375),
    (60, 4.875, 0.375),
    (63, 4.875, 0.375)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Little Ray: Drums continue
drum_notes_continued = [
    (36, 1.5, 0.375),    # Kick on beat 1
    (42, 1.5, 0.375),    # Hihat on &1
    (38, 1.875, 0.375),  # Snare on beat 2
    (42, 1.875, 0.375),  # Hihat on &2
    (36, 2.25, 0.375),   # Kick on beat 3
    (42, 2.25, 0.375),   # Hihat on &3
    (38, 2.625, 0.375),  # Snare on beat 4
    (42, 2.625, 0.375),  # Hihat on &4
    (36, 3.0, 0.375),    # Kick on beat 1
    (42, 3.0, 0.375),    # Hihat on &1
    (38, 3.375, 0.375),  # Snare on beat 2
    (42, 3.375, 0.375),  # Hihat on &2
    (36, 3.75, 0.375),   # Kick on beat 3
    (42, 3.75, 0.375),   # Hihat on &3
    (38, 4.125, 0.375),  # Snare on beat 4
    (42, 4.125, 0.375),  # Hihat on &4
    (36, 4.5, 0.375),    # Kick on beat 1
    (42, 4.5, 0.375),    # Hihat on &1
    (38, 4.875, 0.375),  # Snare on beat 2
    (42, 4.875, 0.375),  # Hihat on &2
    (36, 5.25, 0.375),   # Kick on beat 3
    (42, 5.25, 0.375),   # Hihat on &3
    (38, 5.625, 0.375),  # Snare on beat 4
    (42, 5.625, 0.375)   # Hihat on &4
]

for note, start, duration in drum_notes_continued:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Sax solo (whisper to cry)
sax_notes = [
    (63, 1.5, 0.1875),   # F (whisper)
    (65, 1.6875, 0.1875), # G (build)
    (63, 1.875, 0.1875),  # F
    (61, 2.0625, 0.1875), # E♭
    (63, 2.25, 0.1875),   # F
    (65, 2.4375, 0.1875), # G
    (63, 2.625, 0.1875),  # F
    (60, 2.8125, 0.1875), # E (cry)
    (63, 3.0, 0.1875),    # F
    (65, 3.1875, 0.1875), # G
    (63, 3.375, 0.1875),  # F
    (61, 3.5625, 0.1875), # E♭
    (63, 3.75, 0.1875),   # F
    (65, 3.9375, 0.1875), # G
    (63, 4.125, 0.1875),  # F
    (60, 4.3125, 0.1875), # E
    (63, 4.5, 0.1875),    # F
    (65, 4.6875, 0.1875), # G
    (63, 4.875, 0.1875),  # F
    (61, 5.0625, 0.1875), # E♭
    (63, 5.25, 0.1875),   # F
    (65, 5.4375, 0.1875), # G
    (63, 5.625, 0.1875),  # F
    (60, 5.8125, 0.1875)  # E (final cry)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
