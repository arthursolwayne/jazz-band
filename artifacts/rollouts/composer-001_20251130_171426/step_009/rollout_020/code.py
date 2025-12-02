
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
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5)
    hihat_2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, snare, hihat, hihat_2, hihat_3, hihat_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# Fm scale: F, Gb, Ab, A, Bb, C, Db
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=61, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# Fm7: F, Ab, Bb, C
# Bb7: Bb, Db, F, G
# Fm7 on 2 and 4
chord1 = pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875)  # F
chord1_2 = pretty_midi.Note(velocity=90, pitch=51, start=1.5, end=1.875)  # Ab
chord1_3 = pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875)  # Bb
chord1_4 = pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875)  # C

chord2 = pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375)  # Bb
chord2_2 = pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.375)  # Db
chord2_3 = pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375)  # F
chord2_4 = pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375)  # G

piano.notes.extend([chord1, chord1_2, chord1_3, chord1_4, chord2, chord2_2, chord2_3, chord2_4])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5)
    hihat_2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, snare, hihat, hihat_2, hihat_3, hihat_4])

# Dante: Motif - start it, leave it hanging, come back and finish it
# Fm motif: F, Ab, Bb, B, Ab, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=61, start=2.625, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=61, start=5.625, end=6.0),  # B
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
