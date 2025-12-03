
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
drum_hihat = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: walking line (F2-A2, MIDI 53-57)
bass_note1 = pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875)
bass_note2 = pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25)
bass_note3 = pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625)
bass_note4 = pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0)
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_note1 = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0)
piano_note2 = pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0)
piano_note3 = pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0)
piano_note4 = pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0)
piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_kick3 = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.999)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
drum_snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375)
drum_hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0)
drums.notes.extend([drum_kick2, drum_kick3, drum_snare2, drum_snare3, drum_hihat2])

# Dante: Tenor sax, one short motif, make it sing
# Motif: F (69), G (71), Bb (70), F (69)
sax_note1 = pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75)
sax_note2 = pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0)
sax_note3 = pretty_midi.Note(velocity=110, pitch=70, start=2.0, end=2.25)
sax_note4 = pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5)
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4])

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: walking line (F2-A2, MIDI 53-57)
bass_note5 = pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375)
bass_note6 = pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75)
bass_note7 = pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125)
bass_note8 = pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5)
bass.notes.extend([bass_note5, bass_note6, bass_note7, bass_note8])

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_note5 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5)
piano_note6 = pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5)
piano_note7 = pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5)
piano_note8 = pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5)
piano.notes.extend([piano_note5, piano_note6, piano_note7, piano_note8])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick4 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_kick5 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)
drum_snare4 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
drum_snare5 = pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875)
drum_hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5)
drums.notes.extend([drum_kick4, drum_kick5, drum_snare4, drum_snare5, drum_hihat3])

# Dante: Tenor sax, leave it hanging
# Motif: G (71), Bb (70), F (69), leave it open
sax_note5 = pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25)
sax_note6 = pretty_midi.Note(velocity=110, pitch=70, start=3.25, end=3.5)
sax_note7 = pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75)
sax.notes.extend([sax_note5, sax_note6, sax_note7])

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: walking line (F2-A2, MIDI 53-57)
bass_note9 = pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875)
bass_note10 = pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25)
bass_note11 = pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.625)
bass_note12 = pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0)
bass.notes.extend([bass_note9, bass_note10, bass_note11, bass_note12])

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: C7 (C, E, G, Bb)
piano_note9 = pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0)
piano_note10 = pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=6.0)
piano_note11 = pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0)
piano_note12 = pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0)
piano.notes.extend([piano_note9, piano_note10, piano_note11, piano_note12])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick6 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_kick7 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
drum_snare6 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
drum_snare7 = pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375)
drum_hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0)
drums.notes.extend([drum_kick6, drum_kick7, drum_snare6, drum_snare7, drum_hihat4])

# Dante: Tenor sax, come back and finish it
# Motif: F (69), G (71), Bb (70), F (69)
sax_note8 = pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75)
sax_note9 = pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=5.0)
sax_note10 = pretty_midi.Note(velocity=110, pitch=70, start=5.0, end=5.25)
sax_note11 = pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5)
sax.notes.extend([sax_note8, sax_note9, sax_note10, sax_note11])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
