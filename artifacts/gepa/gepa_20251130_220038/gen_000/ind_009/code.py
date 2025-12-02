
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
drum_note = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0)
sax.notes.append(sax_note)

# Bass line (walking in Dm)
bass_note = pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0)
bass.notes.append(bass_note)

# Piano (7th chords, comp on 2 and 4)
piano_note = pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625)
piano.notes.append(piano_note)

# Drums (Bar 2: kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for i in [0, 1, 2, 3]:
    kick_start = 1.5 + i * 0.375
    kick_end = kick_start + 0.375
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    drums.notes.append(kick)

    snare_start = 1.5 + i * 0.375 + 0.1875
    snare_end = snare_start + 0.1875
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end)
    drums.notes.append(snare)

    hihat_start = 1.5 + i * 0.375
    hihat_end = hihat_start + 0.1875
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end)
    drums.notes.append(hihat)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody
sax_note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5)
sax.notes.append(sax_note)

# Bass line (walking in Dm)
bass_note = pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.5)
bass.notes.append(bass_note)

# Piano (7th chords, comp on 2 and 4)
piano_note = pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125)
piano.notes.append(piano_note)

# Drums (Bar 3: kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for i in [0, 1, 2, 3]:
    kick_start = 3.0 + i * 0.375
    kick_end = kick_start + 0.375
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    drums.notes.append(kick)

    snare_start = 3.0 + i * 0.375 + 0.1875
    snare_end = snare_start + 0.1875
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end)
    drums.notes.append(snare)

    hihat_start = 3.0 + i * 0.375
    hihat_end = hihat_start + 0.1875
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end)
    drums.notes.append(hihat)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody
sax_note = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0)
sax.notes.append(sax_note)

# Bass line (walking in Dm)
bass_note = pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=6.0)
bass.notes.append(bass_note)

# Piano (7th chords, comp on 2 and 4)
piano_note = pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625)
piano.notes.append(piano_note)

# Drums (Bar 4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for i in [0, 1, 2, 3]:
    kick_start = 4.5 + i * 0.375
    kick_end = kick_start + 0.375
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    drums.notes.append(kick)

    snare_start = 4.5 + i * 0.375 + 0.1875
    snare_end = snare_start + 0.1875
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end)
    drums.notes.append(snare)

    hihat_start = 4.5 + i * 0.375
    hihat_end = hihat_start + 0.1875
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
