
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (MIDI 53) on beat 1, E2 (MIDI 51) on beat 2, G2 (MIDI 55) on beat 3, D2 (MIDI 50) on beat 4
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),
    # Chromatic approach to F2
    pretty_midi.Note(velocity=60, pitch=52, start=1.125, end=1.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging.
# F (MIDI 65), Ab (MIDI 60), Bb (MIDI 62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F2 (MIDI 53) on beat 1, G2 (MIDI 55) on beat 2, Ab2 (MIDI 56) on beat 3, D2 (MIDI 50) on beat 4
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=55, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=56, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),
    # Chromatic approach to F2
    pretty_midi.Note(velocity=60, pitch=54, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Ab7 (Ab, C, Eb, G)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # G
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F2 (MIDI 53) on beat 1, Ab2 (MIDI 56) on beat 2, G2 (MIDI 55) on beat 3, C2 (MIDI 48) on beat 4
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=56, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=6.0),
    # Chromatic approach to F2
    pretty_midi.Note(velocity=60, pitch=54, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    end = start + 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.25)
    # Hi-hat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
