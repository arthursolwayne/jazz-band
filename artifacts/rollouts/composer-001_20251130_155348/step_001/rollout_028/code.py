
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
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.125 + 0.375)
    drums.notes.append(kick)
    # Snare on 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.5 + 0.375)
    drums.notes.append(snare)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
# Bar 2: F - Gb - G - A (F7)
for bar in range(2, 5):
    start = bar * 1.5
    # F (beat 1)
    note = pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 0.375)
    bass.notes.append(note)
    # Gb (beat 2)
    note = pretty_midi.Note(velocity=100, pitch=70, start=start + 0.75, end=start + 0.75 + 0.375)
    bass.notes.append(note)
    # G (beat 3)
    note = pretty_midi.Note(velocity=100, pitch=72, start=start + 1.125, end=start + 1.125 + 0.375)
    bass.notes.append(note)
    # A (beat 4)
    note = pretty_midi.Note(velocity=100, pitch=74, start=start + 1.5, end=start + 1.5 + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: F7 on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    # F7 on beat 2
    note = pretty_midi.Note(velocity=100, pitch=71, start=start + 0.75, end=start + 0.75 + 0.375)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=74, start=start + 0.75, end=start + 0.75 + 0.375)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=76, start=start + 0.75, end=start + 0.75 + 0.375)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=68, start=start + 0.75, end=start + 0.75 + 0.375)
    piano.notes.append(note)
    # F7 on beat 4
    note = pretty_midi.Note(velocity=100, pitch=71, start=start + 1.5, end=start + 1.5 + 0.375)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=74, start=start + 1.5, end=start + 1.5 + 0.375)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=76, start=start + 1.5, end=start + 1.5 + 0.375)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=68, start=start + 1.5, end=start + 1.5 + 0.375)
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.125 + 0.375)
    drums.notes.append(kick)
    # Snare on 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.5 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F - Gb - G - F (start on bar 2, beat 1)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=70, start=1.5 + 0.75, end=1.5 + 0.75 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=1.5 + 1.125, end=1.5 + 1.125 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=70, start=1.5 + 1.875, end=1.5 + 1.875 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=1.5 + 2.25, end=1.5 + 2.25 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 2.625, end=1.5 + 2.625 + 0.375)
sax.notes.append(note)

# Add to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write MIDI file
midi.write("dante_intro.mid")
