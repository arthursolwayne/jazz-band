
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
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice. F7 chord (F A C E)
# F7 = F, A, C, E
# Root motion: F -> Bb -> Eb -> A
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=90, pitch=68, start=2.625, end=3.0), # Bb
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=90, pitch=63, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=90, pitch=63, start=5.625, end=6.0), # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4. F7, Bb7, Eb7, A7
# Bar 2: F7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25), # E
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # A
    # Bar 4: Eb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # D
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F, Bb, Eb, F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=110, pitch=60, start=1.625, end=1.75), # Bb
    pretty_midi.Note(velocity=110, pitch=57, start=1.75, end=1.875), # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.375), # F
    pretty_midi.Note(velocity=110, pitch=60, start=2.375, end=2.5), # Bb
    pretty_midi.Note(velocity=110, pitch=57, start=2.5, end=2.625), # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=2.75), # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
