
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5
for beat in [0, 2]:
    kick = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(kick)
for beat in [1, 3]:
    snare = pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(snare)
for beat in range(8):
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.1875, end=(beat + 1) * 0.1875)
    drums.notes.append(hihat)

# Bars 2-4 (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
# Bar 2: D (38), F# (41) -> E (40)
note1 = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625)
bass.notes.append(note1)
bass.notes.append(note2)
bass.notes.append(note3)

# Bar 3: A (45), C# (48) -> B (47)
note1 = pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=2.875)
note2 = pretty_midi.Note(velocity=100, pitch=48, start=2.875, end=3.25)
note3 = pretty_midi.Note(velocity=100, pitch=47, start=3.25, end=3.625)
bass.notes.append(note1)
bass.notes.append(note2)
bass.notes.append(note3)

# Bar 4: D (38), F# (41) -> E (40)
note1 = pretty_midi.Note(velocity=100, pitch=38, start=3.625, end=3.875)
note2 = pretty_midi.Note(velocity=100, pitch=41, start=3.875, end=4.25)
note3 = pretty_midi.Note(velocity=100, pitch=40, start=4.25, end=4.625)
bass.notes.append(note1)
bass.notes.append(note2)
bass.notes.append(note3)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#), comp on 2 and 4
note1 = pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875)
note3 = pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875)
note4 = pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875)
piano.notes.append(note1)
piano.notes.append(note2)
piano.notes.append(note3)
piano.notes.append(note4)

# Bar 3: A7 (A-C#-E-G), comp on 2 and 4
note1 = pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=2.875)
note2 = pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.875)
note3 = pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.875)
note4 = pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.875)
piano.notes.append(note1)
piano.notes.append(note2)
piano.notes.append(note3)
piano.notes.append(note4)

# Bar 4: Dmaj7 (D-F#-A-C#), comp on 2 and 4
note1 = pretty_midi.Note(velocity=90, pitch=52, start=3.625, end=3.875)
note2 = pretty_midi.Note(velocity=90, pitch=55, start=3.625, end=3.875)
note3 = pretty_midi.Note(velocity=90, pitch=57, start=3.625, end=3.875)
note4 = pretty_midi.Note(velocity=90, pitch=60, start=3.625, end=3.875)
piano.notes.append(note1)
piano.notes.append(note2)
piano.notes.append(note3)
piano.notes.append(note4)

# You: Tenor sax — one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F# - A - D (MIDI 62, 65, 67, 62) on beat 1, then repeat on beat 3
note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0)
note5 = pretty_midi.Note(velocity=110, pitch=62, start=3.625, end=3.875)
note6 = pretty_midi.Note(velocity=110, pitch=65, start=3.875, end=4.25)
note7 = pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.625)
note8 = pretty_midi.Note(velocity=110, pitch=62, start=4.625, end=5.0)
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)
sax.notes.append(note4)
sax.notes.append(note5)
sax.notes.append(note6)
sax.notes.append(note7)
sax.notes.append(note8)

# Add the drum fill for bar 2
# Bar 2: Fill on beat 2
fill = pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.25)
drums.notes.append(fill)

# Add the snare fill on beat 3
fill = pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.25)
drums.notes.append(fill)

# Drums continue for remaining bars
for beat in [4, 6]:
    kick = pretty_midi.Note(velocity=100, pitch=36, start=(beat + 1) * 0.375, end=(beat + 2) * 0.375)
    drums.notes.append(kick)
for beat in [5, 7]:
    snare = pretty_midi.Note(velocity=100, pitch=38, start=(beat + 1) * 0.375, end=(beat + 2) * 0.375)
    drums.notes.append(snare)
for beat in range(8, 16):
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.1875, end=(beat + 1) * 0.1875)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
