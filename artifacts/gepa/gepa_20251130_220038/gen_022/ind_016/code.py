
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
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (walking line, chromatic approaches, no repeat notes)
# D minor 7th chord: Dm7 = D F A C
# Walking bass line starting on D and descending chromatically
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),   # D4
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),  # C#4
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # C4
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),   # B3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),   # D4
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.75),  # C#4
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # C4
    pretty_midi.Note(velocity=100, pitch=59, start=4.125, end=4.5),   # B3
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),   # D4
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25),  # C#4
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # C4
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),   # B3
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# D7 = D F# A C
# Comp on 2 and 4 of each bar
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),   # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),   # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),   # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),   # C5
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),   # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),   # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),   # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),   # C5
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),   # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),   # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),   # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),   # C5
]
piano.notes.extend(piano_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2, 4):
    bar_start = i * 1.5
    kick_start = bar_start + 0.0
    snare_start = bar_start + 0.75
    hihat_start = bar_start
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.125)
    for j in range(8):
        hihat_copy = hihat.copy()
        hihat_copy.start = hihat_start + j * 0.125
        hihat_copy.end = hihat_copy.start + 0.125
        drums.notes.append(hihat_copy)
    drums.notes.extend([kick, snare])

# Dante on sax: motif that sings, start it, leave it hanging, come back and finish it
# Motif: D -> F -> B -> D (Dm7 arpeggio, but with a twist)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),   # D4 (hanging)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),   # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
