
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0), # F
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.5), # Bb
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875), # B
    pretty_midi.Note(velocity=80, pitch=73, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.625), # C#
    pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0), # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = []
# Bar 2 (beat 2)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625), # F
])
# Bar 3 (beat 2)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=73, start=3.75, end=4.125), # C
])
# Bar 4 (beat 2)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625), # F#
    pretty_midi.Note(velocity=100, pitch=81, start=5.25, end=5.625), # B
])
piano.notes.extend(piano_notes)

# Sax: your motif - short, singable, with tension
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.6875), # A
    pretty_midi.Note(velocity=110, pitch=71, start=1.6875, end=1.875), # B
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.0), # C
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.1875), # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.1875, end=3.375), # A
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.5625), # B
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.6875), # C
    pretty_midi.Note(velocity=110, pitch=69, start=4.6875, end=4.875), # A
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0), # G
    # Return to the motif
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.1875), # A
    pretty_midi.Note(velocity=110, pitch=71, start=5.1875, end=5.375), # B
    pretty_midi.Note(velocity=110, pitch=72, start=5.375, end=5.5625), # C
    pretty_midi.Note(velocity=110, pitch=74, start=5.5625, end=5.75), # D
    pretty_midi.Note(velocity=110, pitch=72, start=5.75, end=6.0), # C
]
sax.notes.extend(sax_notes)

# Drums: continue pattern for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
