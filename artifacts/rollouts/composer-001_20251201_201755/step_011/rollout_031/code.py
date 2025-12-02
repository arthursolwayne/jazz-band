
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Fill the bar with kick, snare, and hihat
for note in pretty_midi.Note.velocity_from_midi(100):
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
    drums.notes.append(kick)

    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0)
    drums.notes.append(snare)

    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=i * 0.375, end=i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) with chromatic approach to G2 (MIDI 43)
bass_note = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.125)  # chromatic approach
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=43, start=2.125, end=2.5)
bass.notes.append(bass_note)

# Piano: Open voicing on Dm7 (F, A, C, D)
piano_note = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0)  # F4
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=2.0)  # A4
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0)  # C5
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0)  # D4
piano.notes.append(piano_note)

# Sax: Motif - D4 (MIDI 62), F4 (MIDI 65), G4 (MIDI 67), D4 (MIDI 62)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5)
sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: C2 (MIDI 36) with chromatic approach to D2 (MIDI 38)
bass_note = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=37, start=3.375, end=3.625)  # chromatic approach
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=38, start=3.625, end=4.0)
bass.notes.append(bass_note)

# Piano: Open voicing on Gm7 (Bb, D, F, G)
piano_note = pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.5)  # Bb4
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5)  # D4
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5)  # F4
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5)  # G4
piano.notes.append(piano_note)

# Sax: Motif variation - G4 (MIDI 67), Bb4 (MIDI 62), D4 (MIDI 65), G4 (MIDI 67)
sax_note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0)
sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (MIDI 38) with chromatic approach to F2 (MIDI 41)
bass_note = pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.125)  # chromatic approach
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=41, start=5.125, end=5.5)
bass.notes.append(bass_note)

# Piano: Open voicing on Cm7 (Eb, G, Bb, C)
piano_note = pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=5.0)  # Eb4
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0)  # G4
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0)  # Bb4
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0)  # C5
piano.notes.append(piano_note)

# Sax: Motif resolution - D4 (MIDI 62), F4 (MIDI 65), G4 (MIDI 67), D4 (MIDI 62)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5)
sax.notes.append(sax_note)

# Drums: kick, snare, hihat (same pattern)
for note in pretty_midi.Note.velocity_from_midi(100):
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
    drums.notes.append(kick)

    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=6.375, end=6.5)
    drums.notes.append(snare)

    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=4.5 + i * 0.375, end=4.5 + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
